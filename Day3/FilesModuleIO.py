import fnmatch
import os
import shutil
from datetime import datetime
from glob import glob
from pathlib import Path
from tempfile import TemporaryDirectory, TemporaryFile

from genericpath import isfile

# with open("demo.txt", mode="a") as f:
#     f.write("Some demo text for testing")

# with open("demo.txt", mode="r") as f:
#     print(f.read())

# * path = os.getcwd()

# ? First method to list directories and files in python
# first_entries = os.listdir("Que1/")
# for entry in first_entries:
#     print(entry)
# print("--------First Method Ends")

# ? Second method to list directories and files in python
# with os.scandir("Day3/") as second_entries:
#     for entry in second_entries:
#         print(entry.name)
# print("--------Second Method Ends")

# ? Third method to list directories and files in python
# ? This line returns iterator of python so we have to use iterdir()
# entries = Path("Day2/")
# for entry in entries.iterdir():
#     # ? Full entry object will return full path but entry.name returns name of the file
#     print(entry.name)
# print("--------Third Method Ends")


# ! To find absolute path to parent dir
# * parent_dir_path = os.path.abspath(os.path.join(path, os.pardir))

# print(parent_dir_path)

# ? Listing only files not directories using scandir
# basepath = "Day2/"
# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)

# * Listing files using Pathlib

# entries = Path(basepath)
# files_in_basepath = (entry for entry in entries.iterdir() if entry.is_file())
# for file_name in files_in_basepath:
#     info = file_name.stat()
# ! below line is used for formating date
#     print(datetime.fromtimestamp(info.st_mtime).strftime("%d-%m-%Y %X"))
#     print(file_name.name, end=" ")
#     print(info.st_size)
# print(file_name.name)

# * Listing sub directories using pathlib
# entries = Path(basepath)
# subdir_basepath = (entry for entry in entries.iterdir() if entry.is_dir())
# for dir_name in subdir_basepath:
#     info = dir_name.stat()
#     # ! Print modified time of a file
#     print(datetime.fromtimestamp(info.st_mtime).strftime("%d-%m-%Y %X"))
#     print(dir_name.name)

# ? Making Directories
# p = Path("Day3/my_new_dir")
# p.mkdir(exist_ok=True)

# os.makedirs("Day3/grand_father/father/child", mode=0o770)

# ! File Name pattern matching
# ? endswith and startswith
# ? pathlib.Path.glob()

basepath = "Day3/some_directory"

entries = Path(basepath)
# txt_file_name = (file for file in entries.iterdir() if file.name.endswith("txt"))
# for txt in txt_file_name:
#     print(txt.name)

# txt_file_name_contains_backup = (
#     file for file in entries.iterdir() if fnmatch.fnmatch(file.name, "*[0-9]*.txt")
# )
# for backup_file in txt_file_name_contains_backup:
#     print(backup_file.name)

# ? We can also use glob function from glob package
# ! os.walk() fn is used to traverse on directories
# for dirpath, dirnames, files in os.walk(basepath, topdown=False):
#     print("Found Directory : ", dirpath)
#     for file in files:
#         print(file)

# ! Making temporary files and Directories

# ? we can use with clause in TemporaryFile
# fp = TemporaryFile("w+t")
# fp.write("My Temp text")
# fp.seek(0)
# print(fp.read())
# fp.close()

# with TemporaryFile("w+t") as fp:
#     fp.write("My files")
#     fp.seek(0)
#     print(fp.read())

# with TemporaryDirectory() as fd:
#     print("Temporary Directory Created ...", fd)
#     print(os.path.exists(fd))

# file_path = "/home/aakash/Desktop/Python Core Concepts/aakash.txt"
# if os.path.isfile(file_path):
#     os.remove(file_path)
# else:
#     print("Error given file is a not valid file")

# ! Deleting directories
# ? To delete whole folder
# trash_dir = "Day3/some_directory"
# try:
#     shutil.rmtree(trash_dir)
# except OSError as exc:
#     print(f"Error {trash_dir} : {exc.strerror}")

# ! Copying and Renaming Files using shutil

# src = "/home/aakash/Desktop/Python Core Concepts/Day3/my_new_directory/demo.txt"
# dst = "/home/aakash/Desktop/Python Core Concepts/Day3/grand_father/father"

# shutil.copy(src=src, dst=dst)

# print(os.getcwd())

os.chdir("/home/aakash/Desktop/Python Core Concepts/my_testing_folder")

# print(os.getcwd())

Path("data").mkdir(exist_ok=True)

for file in os.listdir():
    # Old method
    # filename, ext = os.path.splitext(file)
    # f = Path(file)
    # filename, ext = f.stem, f.suffix
    # print(filename)
    # print(ext)
    # splitted_file = filename.split("-")
    # new_name = f"{splitted_file[1].zfill(2)}-{splitted_file[0]}-{splitted_file[2]}{ext}"
    # # Old method
    # # os.rename(file, new_name)
    # f.rename(new_name)
    if file == "data":
        continue
    shutil.copy2(file, "data")
