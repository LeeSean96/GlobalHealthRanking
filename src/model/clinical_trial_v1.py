import string


class ClinicalTrialV1:
    def __init__(self):
        self.nct_id: string
        self.url_link: string
        self.lead_sponsor: string
        self.overall_status: string
        self.results_reported: bool
        self.is_overdue: bool
        self.completion_date: string
        self.results_date: string
        self.download_date: string
        self.brief_title: string
        self.population_type: string