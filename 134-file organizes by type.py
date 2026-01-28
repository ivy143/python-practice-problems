# File Organizer by Type
import os
import shutil
from collections import defaultdict
def organize_files_by_type(source_directory, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    file_types = defaultdict(list)

    # Scan the source directory for files
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()
            file_types[file_extension].append(file_path)

    # Create subdirectories and move files
    for file_extension, files in file_types.items():
        type_directory = os.path.join(target_directory, file_extension.lstrip('.'))
        if not os.path.exists(type_directory):
            os.makedirs(type_directory)
        for file_path in files:
            shutil.move(file_path, os.path.join(type_directory, os.path.basename(file_path)))
# Example usage
source_dir = 'source_files'  # Directory containing files to organize
target_dir = 'organized_files'  # Directory where organized files will be placed
organize_files_by_type(source_dir, target_dir)
print(f"Files organized by type in: {target_dir}")
# Note: Ensure 'source_files' directory exists with files for testing.
