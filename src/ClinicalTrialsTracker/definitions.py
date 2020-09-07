import logging
import os
from pathlib import Path

# CURRENT
ROOT_DIR = str(Path(os.path.abspath(__file__)).parents[2])
CSV_DELIMITER = ';'
CSV_QUOTE_CHAR = '"'
CLINICAL_TRIAL_FILENAME = 'ClinicalTrialsResults.csv'

# Logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Domain values
UNCERTAINTY = 30  # days
REPORTING_THRESHOLD = 365 + UNCERTAINTY  # days
INCONSISTENCY_THRESHOLD = UNCERTAINTY  # days
DEFAULT_REPORTING_TIME_DELAY_PENALTY = 999999  # days

# DEPRECATE
CSV_V1_DELIMITER = ';'
CSV_V1_QUOTE_CHAR = '"'
