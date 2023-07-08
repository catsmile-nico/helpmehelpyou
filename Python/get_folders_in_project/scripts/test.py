import os

# Get the path of the script folder
script_folder = os.path.dirname(os.path.abspath(__file__))
print("script folder: {path}".format(path=script_folder))

# Get the path of the project folder
project_folder = os.path.dirname(script_folder)
print("project folder: {path}".format(path=project_folder))

# Construct the path to the data folder from project folder
data_folder = os.path.join(project_folder, 'data')
print("data folder: {path}".format(path=data_folder))

# Read a file in the data folder
file_path = os.path.join(data_folder, 'example.txt')
with open(file_path, 'r') as file:
    content = file.read()
    print(content)