import os

def get_files_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return []

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Filter only files (excluding directories)
    file_paths = [os.path.join(folder_path, file) for file in file_list if os.path.isfile(os.path.join(folder_path, file))]

    return file_paths

# Replace 'folder_path' with the path to your folder
StudentsData = []


def get_The_Student_Details(files):
    for file in files:
        tmp = file.split("\\")
        fileName = tmp[-1]
        fileName = fileName.split(",")
        name = ' '.join(fileName[0].split('_'))
        id = fileName[-1].split('.')[0]
        StudentsData.append({'Name': name, 'ID': id})
