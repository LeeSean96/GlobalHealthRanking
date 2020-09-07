import logging
import sys
import csv
from pathlib import Path
from typing import TextIO, List

from src.ClinicalTrialsTracker.definitions import CSV_V1_DELIMITER, CSV_V1_QUOTE_CHAR, ROOT_DIR, \
    CLINICAL_TRIAL_FILENAME, CSV_DELIMITER, CSV_QUOTE_CHAR
from src.ClinicalTrialsTracker.model.clinical_trial_v1 import ClinicalTrialV1

from src.ClinicalTrialsTracker.model.clinical_trial import ClinicalTrial, clinical_trial_fieldnames


def clinical_trial_v1_to_clinical_trial():
    """Entry point for the main application script."""
    logging.info('Starting')
    clinical_trial_v1_filepath = sys.argv[1]
    clinical_trials: List[ClinicalTrial] = []
    clinical_trial_v1_filestream: TextIO
    logging.info('Reading input file %s' % clinical_trial_v1_filepath)
    with open(clinical_trial_v1_filepath) as clinical_trial_v1_filestream:
        clinical_trial_v1_csvreader = csv.DictReader(clinical_trial_v1_filestream,
                                                     delimiter=CSV_V1_DELIMITER,
                                                     quotechar=CSV_V1_QUOTE_CHAR)
        for clinical_trial_v1_csvrow in clinical_trial_v1_csvreader:
            clinical_trial_v1_row = ClinicalTrialV1(**clinical_trial_v1_csvrow)
            clinical_trial = ClinicalTrial(clinical_trial_v1_row)
            clinical_trials.append(clinical_trial)

    clinical_trials_output_filepath = Path(ROOT_DIR).joinpath(CLINICAL_TRIAL_FILENAME)
    logging.info('Writing output to %s' % clinical_trials_output_filepath)
    with open(clinical_trials_output_filepath, 'w+') as clinical_trials_output_filestream:
        clinical_trials_output_file_writer = csv.DictWriter(clinical_trials_output_filestream,
                                                            fieldnames=clinical_trial_fieldnames,
                                                            delimiter=CSV_DELIMITER,
                                                            quotechar=CSV_QUOTE_CHAR)
        clinical_trials_output_file_writer.writeheader()
        clinical_trials_output_file_writer.writerows(map(lambda x: x.to_dict(), clinical_trials))

    logging.info('Complete')


if __name__ == '__main__':
    clinical_trial_v1_to_clinical_trial()
