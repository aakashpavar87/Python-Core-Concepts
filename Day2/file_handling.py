import os
# ! Writing to file system
# ? file = open("aakash.txt", "w")
# ? file.write("some demo Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ullam possimus nulla labore, inventore quas laborum provident officia saepe.")
# ? file.close()
path = os.getcwd()
print("Current Directory : ", path)
print("Parent Directory : ", os.path.abspath(os.path.join(path, os.pardir)))

# entries = os.listdir(path=path)
entries = os.listdir(path="Day2/")
print(entries)
# ! print(entries)
# ! Reading to file system

file = open("aakash.txt", "r")
print(file.read())
file.close()


# ! read fn read all text from file
# ! readline fn reads only one line in file
# ! readlines fn reads all lines in file and returns list of lines
