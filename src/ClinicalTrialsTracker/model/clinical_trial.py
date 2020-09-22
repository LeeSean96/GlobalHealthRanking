import string
from datetime import date, datetime
from typing import List

from src.ClinicalTrialsTracker.model import clinical_trial_v1
from src.ClinicalTrialsTracker.model.enum import category, Category
from src.ClinicalTrialsTracker.model.enum import overall_status
from src.ClinicalTrialsTracker.definitions import REPORTING_THRESHOLD, INCONSISTENCY_THRESHOLD, \
    DEFAULT_REPORTING_TIME_DELAY_PENALTY

clinical_trial_fieldnames: List[str] = [
    'nct_id',
    'url_link',
    'lead_sponsor',
    'overall_status',
    'results_reported',
    'is_overdue',
    'completion_date',
    'results_date',
    'download_date',
    'brief_title',
    'category',
    'time_delay',
]


class ClinicalTrial:
    def __init__(self):
        self.nct_id: string
        self.url_link: string
        self.lead_sponsor: string
        self.overall_status: overall_status.OverallStatus
        self.results_reported: bool
        self.is_overdue: bool
        self.completion_date: date = None
        self.results_date: date = None
        self.download_date: date = None
        self.brief_title: string
        self.category: category.Category
        self.time_delay: int

    def __init__(self, v1: clinical_trial_v1.ClinicalTrialV1):
        self.nct_id: string = v1.nct_id
        self.url_link: string = v1.url_link
        self.lead_sponsor: string = v1.lead_sponsor
        self.overall_status: overall_status.OverallStatus = map_overall_status(v1.overall_status)
        self.results_reported: bool = True if v1.results_reported == 'True' else False
        self.is_overdue: bool = True if v1.is_overdue == 'True' else False
        self.completion_date: date = try_parse_iso_date(v1.completion_date)
        self.results_date: date = try_parse_iso_date(v1.results_date)
        self.download_date: date = try_parse_iso_date(v1.download_date)
        self.brief_title: string = v1.brief_title
        self.category: category.Category = self.create_category()
        self.time_delay: int = self.calculate_time_delay()

    @property
    def has_no_reporting_requirements(self) -> bool:
        if self.overall_status == overall_status.OverallStatus.withdrawn or self.overall_status == overall_status.OverallStatus.suspended:
            return True

        return False

    @property
    def has_finished(self) -> bool:
        if self.overall_status == overall_status.OverallStatus.completed or self.overall_status == overall_status.OverallStatus.terminated:
            return True

        return False

    @property
    def is_ongoing(self) -> bool:
        if self.overall_status == overall_status.OverallStatus.not_yet_recruiting \
                or self.overall_status == overall_status.OverallStatus.active_not_recruiting \
                or self.overall_status == overall_status.OverallStatus.recruiting \
                or self.overall_status == overall_status.OverallStatus.enrolling_by_invitation:
            return True

        return False

    @property
    def has_future_completion_date(self) -> bool:
        if self.completion_date is None:
            return False

        if (self.download_date - self.completion_date).days < INCONSISTENCY_THRESHOLD:
            return True

        return False

    @property
    def has_exceeded_reporting_threshold(self) -> bool:
        if self.completion_date is None:
            return True

        if (self.download_date - self.completion_date).days < REPORTING_THRESHOLD:
            return False

        return True

    def create_category(self) -> Category:
        if self.has_no_reporting_requirements:
            return Category.no_reporting_requirement

        if self.has_finished and self.results_reported and self.has_exceeded_reporting_threshold:
            return Category.due_and_reported

        if self.has_finished and not self.results_reported and self.has_exceeded_reporting_threshold:
            return Category.due_but_not_reported

        if self.has_finished and not self.has_exceeded_reporting_threshold:
            return Category.completed_but_not_due

        if self.is_ongoing and self.has_future_completion_date:
            return Category.ongoing

        return Category.inconsistent_data

    def calculate_time_delay(self) -> int:
        if self.category != Category.due_and_reported:
            return None

        if self.results_date is None or self.completion_date is None:
            return DEFAULT_REPORTING_TIME_DELAY_PENALTY

        return (self.results_date - self.completion_date).days + REPORTING_THRESHOLD

    def to_dict(self) -> dict:
        return {
            'nct_id': self.nct_id,
            'url_link': self.url_link,
            'lead_sponsor': self.lead_sponsor,
            'overall_status': self.overall_status.value,
            'results_reported': self.results_reported,
            'is_overdue': self.is_overdue,
            'completion_date': None if self.completion_date is None else self.completion_date.strftime('%Y-%m-%d'),
            'results_date': None if self.results_date is None else self.results_date.strftime('%Y-%m-%d'),
            'download_date': None if self.download_date is None else self.download_date.strftime('%Y-%m-%d'),
            'brief_title': self.brief_title,
            'category': self.category.value,
            'time_delay': self.time_delay,
        }


def try_parse_iso_date(date_string: string) -> datetime:
    try:
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        date = None
    return date


def map_overall_status(status: string) -> overall_status.OverallStatus:
    if status == overall_status.OverallStatus.completed.value:
        return overall_status.OverallStatus.completed
    elif status == overall_status.OverallStatus.withdrawn.value:
        return overall_status.OverallStatus.withdrawn
    elif status == overall_status.OverallStatus.active_not_recruiting.value:
        return overall_status.OverallStatus.active_not_recruiting
    elif status == overall_status.OverallStatus.enrolling_by_invitation.value:
        return overall_status.OverallStatus.enrolling_by_invitation
    elif status == overall_status.OverallStatus.not_yet_recruiting.value:
        return overall_status.OverallStatus.not_yet_recruiting
    elif status == overall_status.OverallStatus.recruiting.value:
        return overall_status.OverallStatus.recruiting
    elif status == overall_status.OverallStatus.suspended.value:
        return overall_status.OverallStatus.suspended
    elif status == overall_status.OverallStatus.unknown_status.value:
        return overall_status.OverallStatus.unknown_status
    elif status == overall_status.OverallStatus.terminated.value:
        return overall_status.OverallStatus.terminated
    else:
        raise Exception('Unknown status %s provided.' % status)
