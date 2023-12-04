import zipfile
import pathlib


def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def save_todos(todos_to_save, filepath='todos.txt'):
    """ write todos in the file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_to_save)


if __name__ == "__main__":
    print("this will only execute if function.py is run directly")
    print("Will not executed if cli.py is run")


def zip_files(filepaths, dest_dir):

    with zipfile.ZipFile(pathlib.Path(dest_dir, "compressed.zip"), 'w') as zipper:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zipper.write(filepath, arcname=filepath.name)


def unzip_files(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as zipper:
        zipper.extractall(dest_dir)