import logging
import os
from pathlib import Path

# CURRENT
ROOT_DIR = str(Path(os.path.abspath(__file__)).parents[1])
CSV_DELIMITER = ';'
CSV_QUOTE_CHAR = '"'
CLINICAL_TRIAL_FILENAME = 'ClinicalTrialsResults.csv'

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# DEPRECATE
CSV_V1_DELIMITER = ';'
CSV_V1_QUOTE_CHAR = '"'
