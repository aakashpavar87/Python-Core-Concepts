import os

# def file_reader(file):
#     for row in open(file, "r"):
#         yield row


os.chdir("/home/aakash/Desktop/Python Core Concepts/Day4")

# for name in file_reader("data.txt"):
#     name_with_out_newline = name.replace("\n", "")
#     if name_with_out_newline == "Bharat":
#         print("Found Bharat Program Terminated")
#         break
#     print(name_with_out_newline)

x = (v for v in range(1, 11))

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# ! with generator comprehension we can make generator on the hand
# ? syntax : (var for var in range() or sequence)

for name in (i for i in open("data.txt", "r")):
    name_with_out_newline = name.replace("\n", "")
    if name_with_out_newline == "Bharat":
        print("Found Bharat Program Terminated")
        break
    print(name_with_out_newline)
