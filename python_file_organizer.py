# Python automation script that organizes files into folders based on their file extensions.

import os
import shutil

# Get the folder path from the user that needs to be organized

directory = input("Enter Folder path to organize: ").strip()

if not os.path.exists(directory):
    print("Error! Unkown Folder Path.")
    exit()

extensions = {
    ".jpg": "Photos",
    ".pdf": "Documents",
    ".xlsx": "Excel",
    ".docx": "Files",
    ".pptx": "Presentations",
    ".png": "Photos",
    ".csv": "Excel"
}

# Iterate through all files in the specified directory

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(filename)[1].lower()
    folder_name = extensions.get(extension, "Others")

    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    destination_path = os.path.join(folder_path, filename)

    if os.path.exists(destination_path):
        name, ext = os.path.splitext(filename)
        counter = 1

        while os.path.exists(destination_path):
            new_filename = f"{name}_copy{counter}{ext}"
            destination_path = os.path.join(folder_path, new_filename)
            counter += 1

    shutil.move(file_path, destination_path)

    print(f"Moved {filename} to {folder_name} folder.")

print("File organization completed.")
