from enum import Enum


class Category(Enum):
    no_reporting_requirements = 'No reporting requirements'
    results_reported = 'Results reported'
    overdue_for_reporting = 'Overdue for reporting'
    results_not_yet_due = 'Results not yet due'
    inconsistent_data = 'Inconsistent data'
