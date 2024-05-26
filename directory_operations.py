import os

def create_directory(path, dirname):
    os.makedirs(os.path.join(path, dirname))

def delete_directory(path, dirname):
    os.rmdir(os.path.join(path, dirname))

def list_directory(path):
    return os.listdir(path)

def change_directory(current_path, target_directory, base_directory):
    new_path = os.path.realpath(os.path.join(current_path, target_directory))
    if os.path.commonpath([new_path, base_directory]) == base_directory:
        return new_path
    else:
        raise PermissionError("Cannot navigate outside of the base directory")
