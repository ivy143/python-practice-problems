#program to safely create a nested directory in Python
import os

# Define the nested directory path
nested_dir_path = "parent_dir/child_dir/grandchild_dir"

# Safely create the nested directory
os.makedirs(nested_dir_path, exist_ok=True)

print(f"Nested directory '{nested_dir_path}' created successfully (if it didn't exist).")