import os
import re

def remove_numeric_prefix(directory):
    # Regular expression pattern to match numeric prefix followed by a hyphen
    pattern = re.compile(r'^\d+-')
    
    # Walk through each folder, subfolder, and file in the directory
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            # Check if the name matches the pattern
            match = pattern.match(name)
            if match:
                # Construct the new name by removing the matched prefix
                new_name = os.path.join(root, pattern.sub('', name))
                old_name = os.path.join(root, name)
                # Rename the file or folder
                os.rename(old_name, new_name)
                print(f"Renamed: {old_name} -> {new_name}")

# Directory path where you want to remove the prefix
directory_path = ".\\docs"

# Call the function to remove the numeric prefix
remove_numeric_prefix(directory_path)
