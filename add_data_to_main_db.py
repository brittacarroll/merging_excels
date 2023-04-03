import pdb
import pandas as pd
import numpy as np
import os

def find_files(filename, search_path):
    result = []

    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))

    if len(result) > 1:
        print('more than one file found')
        pdb.set_trace()
    else:
        result = result[0]

    return result

main_file_to_add_data_to = find_files("filename_main_database", "approximate_dir_of_file")
data_to_add = find_files("excel_getting_data_from", "approximate_dir_of_file")

data = pd.read_excel(data_to_add)
main = pd.read_excel(main_file_to_add_data_to, sheet_name='xx')

# indicate either the specific columns (in list format) or all columns of data to grab from data excel
columns = data.columns
subject_col = 'Subject ID'
excel_name = 'xx'

subjects_in_main = main.loc[(main['Study'] == study_name) & (main['Excel name'] == excel_name)][subject_col].values
# studies_in_main = main['Study'].values
# subjects_in_main = main[subject_col].values

def enter_values(main, index_in_main, val_already_there, val_to_add):
    if not pd.isna(val_already_there) and not val_already_there == 'nan' and not val_already_there == '':
        return main, 'ignore'
    elif val_to_add == 'Not recorded':
        return main, 'ignore'

    else:
        try:
            main.at[index_in_main, col] = val_to_add
        except:
            main[col] = main[col].astype(str)
            main.at[index_in_main, col] = val_to_add

    # value_in_type_of_rna_seq = main.at[index_in_main, 'Type of RNA seq']
    # if pd.isna(value_in_type_of_rna_seq):
    #     main.at[index_in_main, 'Type of RNA seq'] = 'Biopsy RNA seq'

    return main, 'continue'

subjects_not_in_main = []
columns_not_in_main = []
for index, row in data.iterrows():

    subject_id = row[subject_col]

    # If need to get more specific as to which data to grab, can uncomment lines below
    # visit_date = row['Visit Date']
    # visit_type = row['Visit Description']
    # study = row['Study No.']
    # tissue_type = row['Tissue Type']

    if subject_id == 'Missing and never recovered' or subject_id == 'skip' or pd.isna(subject_id):
        continue

    if subject_id not in subjects_in_main:
        subjects_not_in_main.append(subject_id)
        continue

    for col in columns:

        if 'Unnamed' in col:
            continue

        if col not in main.columns and 'Race' not in col:
            continue

        val_to_add = row[col]

        # formatting dates
        if col == 'DOB' and not pd.isna(val_to_add):
            if val_to_add == '-':
                continue
            else:
                val_to_add = pd.to_datetime(val_to_add)

        if 'Race (choice=' in col:
            if val_to_add == 'Checked':
                val_to_add = col.split('=')[1]
                col = 'Race'
            elif val_to_add == 'Unchecked':
                continue

        # grab the index of the row in main that exactly matches the subject ID, study, etc in data (source) excel
        index_in_main = main.index[(main[subject_col] == subject_id) & (main['Study'] == study) & (main['Excel name'] == excel_name)]
        # index_in_main = main.index[(main[subject_col] == subject_col) & (main['Study'] == study) & (main['Tissue Type'] == tissue_type)].values
        # index_in_main = main.index[(main[subject_col] == subject_id) & (main['Study'] == study_name)].values

        for index in index_in_main:
            val_already_there = main.at[index, col]
            main, response = enter_values(main, index, val_already_there, val_to_add)
            if response == 'ignore':
                continue

main.to_excel('name_of_new_excel.xlsx', index=False)

