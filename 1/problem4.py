import os

def print_directory_contents(path):
    try:
        # List all the files and directories in the specified path
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

# Replace 'your_directory_path' with the path of the directory you want to list
directory_path = '/Users/Dell'
print_directory_contents(directory_path)
