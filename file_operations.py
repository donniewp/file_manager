import os
import shutil

def create_file(path, filename):
    with open(os.path.join(path, filename), 'w') as f:
        pass

def read_file(path, filename):
    with open(os.path.join(path, filename), 'r') as f:
        return f.read()

def write_file(path, filename, content):
    with open(os.path.join(path, filename), 'w') as f:
        f.write(content)

def delete_file(path, filename):
    os.remove(os.path.join(path, filename))

def copy_file(src_path, dest_path, filename):
    shutil.copy(os.path.join(src_path, filename), os.path.join(dest_path, filename))

def move_file(src_path, dest_path, filename):
    shutil.move(os.path.join(src_path, filename), os.path.join(dest_path, filename))

def rename_file(path, old_filename, new_filename):
    os.rename(os.path.join(path, old_filename), os.path.join(path, new_filename))
