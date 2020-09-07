import logging
import sys
import os
import csv
from typing import TextIO, List

from src.ClinicalTrialsTracker.definitions import CSV_V1_DELIMITER, CSV_V1_QUOTE_CHAR, ROOT_DIR
from src.ClinicalTrialsTracker.model.clinical_trial_v1 import ClinicalTrialV1

from src.ClinicalTrialsTracker.model.clinical_trial import ClinicalTrial


def clinical_trial_v1_to_clinical_trial():
    """Entry point for the main application script."""
    print(ROOT_DIR)
    clinical_trial_v1_filepath = sys.argv[1]
    clinical_trials: List[ClinicalTrial]
    clinical_trial_v1_filestream: TextIO
    with open(clinical_trial_v1_filepath) as clinical_trial_v1_filestream:
        clinical_trial_v1_csvreader = csv.DictReader(clinical_trial_v1_filestream,
                                                     delimiter=CSV_V1_DELIMITER,
                                                     quotechar=CSV_V1_QUOTE_CHAR)
        for clinical_trial_v1_csvrow in clinical_trial_v1_csvreader:
            clinical_trial_v1_row = ClinicalTrialV1(**clinical_trial_v1_csvrow)
            clinical_trial = ClinicalTrial(clinical_trial_v1_row)


if __name__ == '__main__':
    clinical_trial_v1_to_clinical_trial()
