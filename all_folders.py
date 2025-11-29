
import os
root_dir = '.'  # Start from the current directory
for dir_path, dir_names, file_names in os.walk(root_dir):
    print(f"Directory: {dir_path}")
    for dir_name in dir_names:
        print(f"  Subdirectory: {dir_name}")
    for file_name in file_names:
        print(f"  File: {file_name}")