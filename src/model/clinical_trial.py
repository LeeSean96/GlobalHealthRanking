import string
from datetime import date

from src.model.enum.category import Category
from src.model.enum.overall_status import OverallStatus


class ClinicalTrial:
    def __init__(self):
        self.nct_id: string
        self.url_link: string
        self.lead_sponsor: string
        self.overall_status: OverallStatus
        self.results_reported: bool
        self.is_overdue: bool
        self.completion_date: date
        self.results_date: date
        self.download_date: date
        self.brief_title: string
        self.category: Category
