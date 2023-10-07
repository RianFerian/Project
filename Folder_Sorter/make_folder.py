import os
import pandas as pd
# # Get the path of the frozen executable
# frozen_path = sys.executable

# # Derive the folder path from the frozen executable path
# base_path = os.path.dirname(frozen_path)

base_path = os.getcwd()
# Get the path of the current Python file

# base_path = os.path.dirname(os.path.abspath(__file__))
base_path = base_path + '\\'

# Specify the base path where the Excel files will be created
# Create empty dataframes and save them as Excel files
df = pd.DataFrame()


for file_name in range(8150, 8178):
    
    try:
        file_path = os.path.join(base_path , str(file_name) + ".xlsx")

        # Create an empty dataframe
        df = pd.DataFrame()

        # Save the dataframe as an Excel file
        df.to_csv(file_path, index=False)

        print("Created Excel file:", file_path)
    except Exception as e:
        print("An error occurred:", str(e))

# pyinstaller Folder_Sorter\make_folder.py --onefile