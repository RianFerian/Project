import os
import shutil

# Base Path
base_path = os.getcwd()
base_path = base_path + '\\'
# base_path = "D:\\Rian\\Template Matching\\Folder_Sorter\\New folder\\"

# Make Folder
folder_names = ['Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Sumatra Utara', 'Sumatra Barat']
for folder_name in folder_names:
    folder_path = os.path.join(base_path, folder_name)
    
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

# Get a list of folders in the current directory
files = os.listdir(base_path)

# Folder Dictionary
folder_mappings = {
    'Jakarta': ['8003', '8001', '8002'],
    'Jawa Barat': ['8003', '8004', '8005', '8006', '8007', '8008', '8009', '8010'],
    'Jawa Tengah': ['8011', '8012', '8013', '8014', '8015'],
    'Sumatra Utara': ['8016', '8017', '8018'],
    'Sumatra Barat': ['8019', '8020', '8021']
}

file_mapping = {"8001":"Jakarta Pusat", "8002":"Jakarta Barat", "8003":"Jakarta Utara",
            "8004":"Bandung", "8005":"banten", "8006":"Bekasi", "8007":"Bogor", "8008":"Sukabumi", "8009":"Indramayu", "8010":"Cirebon",
            "8011":"Brebes", "8012":"Tegal", "8013":"Kudus", "8014":"Semarang", "8015":"Boyolali",
            "8016":"Dairi", "8017":"Karo", "8018":"Nias",
            "8019":"Mentawai", "8020":"Padang", "8021":"Bukittinggi"}


# Move file to destination folder
# Take every file in folder
for file in files:
    # Take destination folder and folder list
    try:
        code, _ = file.split(".")
    except KeyError:
        pass
    for destination_folder, folder_list in folder_mappings.items():
        if code in folder_list:
            source_file = base_path + file
            destination_folder_path = base_path + destination_folder +"\\" + code +" " + file_mapping[code] +".xlsx"
            shutil.move(source_file, destination_folder_path)
            break

# pyinstaller Folder_Sorter\folder_sorter.py --onefile
