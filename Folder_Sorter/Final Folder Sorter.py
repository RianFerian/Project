import os
import shutil
import pandas as pd

# Base Path
base_path = os.getcwd()
base_path = base_path + '\\'

# base_path = "D:\\Rian\\Template Matching\\Folder_Sorter\\New folder\\"
# base_path = "C:\\Users\\rianf\\OneDrive\\Desktop\\Python Projects\\Folder_Sorter\\"


# # Read File Name
map_file_path = base_path + "File Path.xlsx"
# map_file_path = "D:\\Users\\rian.ferian\\Desktop\\Project\\Folder_Sorter\\File Path.xlsx"
file_name = pd.read_excel(map_file_path)
Code = file_name["Code"]
Folder = file_name["Folder"].unique()
Name = file_name["Name File"]

# Make Folder
for folder_name in Folder:
    # Combine base path with folder name to make a new folder
    folder_path = os.path.join(base_path, folder_name)
    
    try:
        # Make Directory
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

# Get a list of folders in the current directory
files = os.listdir(base_path)

# Folder Dictionary
folder_code = file_name[["Folder", "Code"]]

# Iterate through the data and populate the dictionary
folder_mapping = {}
for index, row in folder_code.iterrows():
    key = row['Folder']
    value = str(row['Code'])
    
    if key in folder_mapping:
        folder_mapping[key].append(str(value))
    else:
        folder_mapping[key] = [value] 

# File Mapping
file_mapping = dict(zip(Code, Name))

# Move file to destination folder
# Take every file in main folder
for file in files:
    # Take destination folder and folder list
    try:
        # Take the code only, remove .xlsx
        code, _ = file.split(".")
        for folder_destination, folder_codes  in folder_mapping.items():
            if code in folder_codes:
                source_file = base_path + file
                # Destination Path
                folder_destination_path = base_path + folder_destination +"\\" + code +" " + file_mapping[int(code)] +".xlsx"
            
                # Move file from source path to destination path
                shutil.move(source_file, folder_destination_path)
                break
    except ValueError:
        pass
# # pyinstaller Folder_Sorter\folder_sorter3.py --onefile