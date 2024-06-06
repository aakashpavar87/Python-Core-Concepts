import os
from contextlib import contextmanager

"""
class File:
    def __init__(self, filename, mode):
        os.chdir("Day5/ContextManagerPrac/")
        self.file = open(filename, mode)

    def __enter__(self):
        print("Started")
        return self.file

    def __exit__(self, type, value, traceback):
        print("Ended")
        self.file.close()
        # return True
"""

# ! We have created context manager so we can use with keyword
"""
with File("new.txt", "w") as f:  # type: ignore
    print("Middle Process")
    f.write("Nothing but written data in context manager.")
    # raise Exception("Something got broke")
"""

# ! We can create context manager with inbuilt library context manager  decorator

# * Below code will fine as above code it is new syntax of writing context manager


@contextmanager
def file(filename, mode):
    os.chdir("Day5/ContextManagerPrac/")
    print("Here we can perform some logic before OPn ...")
    f = open(filename, mode)
    yield f
    f.close()
    print("Exit from context manager...")


with file("modern.txt", "w") as f1:
    print("Middle process")
    f1.write("Modern syntax python code...")
