import os
import zipfile
from pathlib import Path

# /home/aakash/Desktop/Python Core Concepts/Day3/my_new_dir

os.chdir("/home/aakash/Desktop/Python Core Concepts/Day3/my_new_dir")

with Path("php files/") as files:
    new_zip = zipfile.ZipFile("new.zip", "w")
    for name in files.iterdir():
        new_zip.write(name)
    new_zip.close()

# with zipfile.ZipFile("data.zip", "r") as zip_obj:
#     for name in zip_obj.namelist():
#         print(name)


# data_zip = zipfile.ZipFile("data.zip", "r")

# ! If we want to unzip password protected file than use pwd= arguments in extract or extractall method

# data_zip.extractall("extracted_dir/")

# print(os.listdir("."))

# data_zip.close()
