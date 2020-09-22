from enum import Enum


class Category(Enum):
    no_reporting_requirement = 'No reporting requirement'
    due_and_reported = 'Due and reported'
    due_but_not_reported = 'Due but not reported'
    completed_but_not_due = 'Completed but not due'
    ongoing = 'Ongoing'
    inconsistent_data = 'Inconsistent data'
