import os
import sys
import xml.etree.ElementTree as ET
import csv
from datetime import *
import warnings

import definitions

# pathworks
my_path = definitions.ROOT_DIR
target = os.path.join(my_path, 'Result.csv')
data_path = os.path.join(my_path, 'data')
targetfile = open(target, 'w+')
csv_output = csv.writer(targetfile, delimiter=';')


# the main parser-anlyser
def parser(filename):

    #setting up parser
    tree = ET.parse(filename)
    root = tree.getroot()
    # Filtering study type for interventional studies only
    study_type = root.find('study_type').text
    if study_type != 'Interventional':
        print('interventional')
        return

    #extracting data
    lead_sponsor = root.find('sponsors').find('lead_sponsor').find('agency').text
    url_link = root.find('required_header').find('url').text
    nct_id = root.find('id_info').find('nct_id').text
    overall_status = root.find('overall_status').text
    brief_title = root.find('brief_title').text
    try:
        completion_date = root.find('primary_completion_date').text
        completion_date = datetime.strptime(completion_date, '%B %Y')
        completion_date_f = completion_date.strftime("%Y-%m-%d")
    except ValueError:
        completion_date = datetime.strptime(completion_date, "%B %d, %Y")
        completion_date_f = completion_date.strftime("%Y-%m-%d")
    except AttributeError:
        completion_date = "Not given"
        completion_date_f = completion_date

    download_date = root.find('required_header').find('download_date').text
    download_date = download_date[42:]
    download_date = datetime.strptime(download_date, '%B %d, %Y')
    download_date_f = datetime.strftime(download_date, "%Y-%m-%d")

    try:
        # clinical results exists
        results_reported = True
        results_date = root.find('results_first_submitted').text
        results_date = datetime.strptime(results_date, '%B %d, %Y')
        results_date_f = results_date.strftime("%Y-%m-%d")
        if overall_status == "Withdrawn": # status withdrawn
            population_type = "4-result posted and not due"
            is_overdue = False
        else: # status not withdrawn
            if completion_date == "Not given":
                population_type = "1-result posted and overdue"
                is_overdue = True
            else:
                difference = download_date - completion_date
                if difference.days < 395:
                    population_type = "4-result posted and not due"
                    is_overdue = False
                else:
                    population_type = "1-result posted and overdue"
                    is_overdue = True
        print(results_date)
    except AttributeError:
        # clinical results do not exist
        results_date_f = 'No'
        results_reported = False
        if overall_status == "Withdrawn": # status withdrawn
            is_overdue = False
            population_type = "3-no result and not yet overdue"
        else: # status not withdrawn
            if completion_date == "Not given":
                population_type = "2-no result and overdue"
                is_overdue = True
            else:
                difference = download_date - completion_date
                if difference.days < 395:
                    population_type = "3-no result and not yet overdue"
                    is_overdue = False
                else:
                    population_type = "2-no result and overdue"
                    is_overdue = True

    datachunk = (nct_id, url_link, lead_sponsor, overall_status, results_reported, is_overdue, completion_date_f, results_date_f, download_date_f, brief_title, population_type)
    csv_output.writerow(datachunk)
    return

warnings.warn('Use raw_data_to_clinical_trial instead.', DeprecationWarning)
minworkdone = 0
# Table Headers
table_header = ("nct_id", "url_link", "lead_sponsor", "overall_status", "results_reported", "is_overdue", "completion_date", "results_date", "download_date", "brief_title", "population_type")
csv_output.writerow(table_header)

# Running script
for temp in os.listdir(data_path)[0:]:
    if (temp != 'AllPublicXML.zip') & (temp != 'Contents.txt') & (temp[0] != '.'):
        temp_path = os.path.join(data_path, temp)
        for filename in os.listdir(temp_path):
            filepath = os.path.join(temp_path, filename)
            print(filepath)
            parser(filepath)

targetfile.close()
print('Done')
