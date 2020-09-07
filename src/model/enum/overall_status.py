from enum import Enum


class OverallStatus(Enum):
    not_yet_recruiting = 'Not yet recruiting'
    recruiting = 'Recruiting'
    enrolling_by_invitation = 'Enrolling by invitation'
    active_not_recruiting = 'Active, not recruiting'
    completed = 'Completed'
    suspended = 'Suspended'
    terminated = 'Terminated'
    withdrawn = 'Withdrawn'
    unknown_status = 'Unknown Status'
