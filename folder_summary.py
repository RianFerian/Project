import os
import shutil
import pandas as pd

# Base Path
base_path = os.getcwd()
base_path = base_path + '\\'
# base_path = "D:\\Rian\\Template Matching\\Folder_Sorter\\New folder\\"

# Take every file in 
files = os.listdir(base_path)

# Get the list of folders in the given path
folder_list = [folder for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))]

# Iterate over each folder
for folder in folder_list:
    folder_path = os.path.join(base_path, folder)  # Get the full path of the folder
    file_list = os.listdir(folder_path)  # Get the list of files in the folder
    for file in file_list:
        try:
            opened_file = pd.read_(folder_path & "\\" & file)
            
        except:
            pass
