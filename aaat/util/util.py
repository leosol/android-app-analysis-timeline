
import os


def list_all_files_from_dir(directory_path, base_dir=None, collected_files=[]):
    if base_dir is not None:
        file_path = os.path.join(base_dir, directory_path)
    else:
        file_path = directory_path
    for root, dirs, files in os.walk(file_path):
        for file in files:
            file_path_item = os.path.join(root, file)
            collected_files.append(file_path_item)
        for dir_item in dirs:
            dir_path_item = os.path.join(root, dir_item)
            list_all_files_from_dir(dir_path_item, collected_files=collected_files)
    if os.path.exists(file_path):
        collected_files.append(file_path)
    return collected_files

def destroy_dir_files(directory_path, base_dir=None):
    if base_dir is not None:
        file_path = os.path.join(base_dir, directory_path)
    else:
        file_path = directory_path
    for root, dirs, files in os.walk(file_path):
        for file in files:
            file_path_item = os.path.join(root, file)
            try:
                os.remove(file_path_item)
            except Exception as e:
                print(f"Error removing {file_path_item}: {e}")
        for dir_item in dirs:
            dir_path_item = os.path.join(root, dir_item)
            try:
                destroy_dir_files(dir_path_item)
            except Exception as e:
                print(f"Error removing {dir_path_item}: {e}")
    try:
        if os.path.exists(file_path):
            os.removedirs(file_path)
    except Exception as e:
        print(f"Error removing {file_path}: {e}")