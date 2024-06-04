import os
import shutil
from pathlib import Path

os.chdir("/home/aakash/Desktop/Python Core Concepts/Day3/my_new_dir")

exts = [".py", ".php", ".txt"]
for file in os.listdir():
    f = Path(file)
    filename, ext = f.stem, f.suffix

    if ext in exts:
        folder_name = f"{ext[1:]} files"
        folder = Path(folder_name)
        folder.mkdir(exist_ok=True)
        shutil.move(src=file, dst=folder_name)
