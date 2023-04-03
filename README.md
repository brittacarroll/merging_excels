## Purpose of this script:
### This Python script is useful for combining two different excels into one. The excels can range in size, and the columns of data pulled from one excel into the other should be indicated (details below).

### There are two excels whose filenames and paths to parent directories must be indicated:
* Those excels are 'main_file_to_add_data_to' and 'data_to_add' (currently on lines 21 and 22).
* Example: main_file_to_add_data_to = find_files("filename_main_database", "approximate_path_to_file's_parent_directory" (can be levels above file's direct parent directory). Add in the excel filenames and paths for both.
* Make sure that certain columns that you are trying to match between the excels have the same exact names. In order to find a particular row in the main database that matches the source data excel, it is necessary to find the exact 'Subject ID', and maybe other information like tissue type or age, to make sure that data is added in for the correct subject. For example, the 'Subject ID' column in both the main database that you are adding data to and in the source excel should be the same (i.e. both 'Subject ID'.)
* Within the script, at this line `columns = data.columns` (currently line 28), you can indicate the columns in the source data excel that you would like to add to the main excel. This can be all the columns (data.columns) or a list of specific ones. If a column from the source excel is not in the main excel, it will be created in the excel that is produced.

### Running the script
* Indicate the name of the output excel on the last line of the script.
* To run, simply input into the terminal: `python3 add_data_to_main_db.py`


