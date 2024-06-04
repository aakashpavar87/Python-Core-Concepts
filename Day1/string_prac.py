#   String methods practice


def myFunction(data):
    print("In my Function ", len(data))

    reversed_string = ""
    for i in range(len(data) - 1, -1, -1):
        reversed_string += data[i]
    return reversed_string


def secondFunction(data):
    return data[::-1]
    # return reversed(data)


# print(myFunction('Aakash'))

# print(secondFunction('Bhavesh'))


# Printing Table pattern


def printTable():
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j == 0 or j == 2:
                print(numbers[i] ** 1, end="\t ")
            elif i == 1:
                print(numbers[i] ** 0, end="\t ")
            else:
                print(numbers[i] ** (j - 1), end="\t ")
        print()


# printTable()


# ! In - Built String Methods

a_str = "Aakash"

print(f"Capitalized Word : {a_str.capitalize()}")

print(f"Count of Letter a : {a_str.count('a')}")

# ? Count Methods have syntax like these str.count('char-sequence', start=,end=)

print(f"Is Name Starts with A : {a_str.startswith('Aa')}")

print(f"Is Name ends with sh : {a_str.endswith('sh')}")

# ? find method returns -1 if value is not found and index method throws error for same

print(f"Index of kar in Name : {a_str.find('kar')}")

print(f"Last Found Index of a in Name : {a_str.rfind('a')}")

print(f"Index of A in Name : {a_str.index('A')}")

print(f"Last Index of A in Name : {a_str.rindex('A')}")


print(f"Swapped Case of strings : {a_str.swapcase()}")

print("tHis is juMMBled tEXt".title())

print("First Line\nSecond Line".splitlines(keepends=False))

print(f"Replace fn of String : {a_str.replace('a', 'A')}")

print("\t\tspaced word\t\t".strip())

print(" , ".join(["c", "cpp", "python"]))
