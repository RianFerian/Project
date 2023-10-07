import os
import shutil

# Base Path
base_path = os.getcwd()
base_path = base_path + '\\'
# base_path = "C:\\Users\\rianf\\OneDrive\\Desktop\\Python Projects\\Folder_Sorter\\"

# # Make Folder
# folder_names = ['Lahat', 'Muara_Rupit', 'Bingin_Teluk', 'Muba', 'Jade']
# for folder_name in folder_names:
#     folder_path = os.path.join(base_path, folder_name)
    
#     try:
#         os.mkdir(folder_path)
#         print(f"Folder '{folder_name}' created successfully.")
#     except FileExistsError:
#         print(f"Folder '{folder_name}' already exists.")

# Get a list of folders in the current directory
files = os.listdir(base_path)
print(files)

# Folder Dictionary
folder_mappings = {
    'Lahat': ['8145', '8146', '8150'],
    'Muara_Rupit': ['8134', '8135', '8136', '8151', '8161', '9420', '9521'],
    'Bingin_Teluk': ['8137', '8138', '8139', '8140', '8142'],
    'Muba': ['8147', '8148', '8149'],
    'Jade': ['8157', '8158', '9020']
}

file_mapping = {"8145":"Arta_Kencana", "8146":"Kencana_Sari", "8150":"Terawas",
            "8134":"Sei_Lakitan", "8135":"Riam_Indah", "8136":"Sei_Gemang", "8151":"Gunung_Bais", "8161":"Mentari_Kulim", "9420":"Kelingi_Lestari", "9521":"Pering_Permai",
            "8137":"Sei_Kepayang", "8138":"Ketapat_Bening", "8139":"Bukit_Hijau", "8140":"Belani_Elok", "8142":"Batu_Cemerlang",
            "8147":"Tirta_Agung", "8148":"Budi_Tirta", "8149":"Suka_Damai",
            "8157":"Sei_Punjung", "8158":"Bangun_Harjo", "9020":"Suka_Bangun"}


# Move file to destination folder
# Take every file in folder
for file in files:
    # Take destination folder and folder list
    try:
        code, _ = file.split(".")
    except ValueError:
        pass

    for destination_folder, folder_list in folder_mappings.items():
        if code in folder_list:
            source_file = base_path + file
            destination_folder_path = base_path + destination_folder +"\\" + code +" " + file_mapping[code] +".xlsx"
            shutil.move(source_file, destination_folder_path)
            break

# pyinstaller Folder_Sorter\folder_sorter_2.py --onefile