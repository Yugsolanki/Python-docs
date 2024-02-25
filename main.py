import os

def add_category_file(directory):
    # Walk through each folder, subfolder, and file in the directory
    for root, dirs, files in os.walk(directory):
        # Check if _category_.json file already exists in the folder
        category_file_path = os.path.join(root, "_category_.json")
        if not os.path.exists(category_file_path):
            # If not present, create _category_.json file with '#' as content
            with open(category_file_path, "w") as f:
                f.write('{\n"label": "Using the Python Interpreter",\n"position": 1,\n"link": {\n"type": "generated-index"\n}\n}')
            print(f"Created _category_.json in: {root}")

# Directory path where you want to add the _category_.json file
directory_path = ".\\docs"

# Call the function to add _category_.json file
add_category_file(directory_path)
