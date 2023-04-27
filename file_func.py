import os
import shutil


def del_dir(path):
    try:
        if os.path.exists(path):
            os.remove(path)
    except FileNotFoundError:
        print("File doesnt exist")
    except PermissionError:
        print("You don't have permission to delete that file")
    except OSError:
        print("That folder contains files")


def del_file(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)


def cmp_files(file1, file2):
    return True if file1 == file2 else False


def move_file(file, directory):
    shutil.move(file, directory)


def rename(path, name):
    new_name = os.path.join(path, name)
    os.renames(path, new_name)

