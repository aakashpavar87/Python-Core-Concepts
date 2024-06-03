my_list = [("one", 1), ("two", 2), ("three", 3)]

# ! We can spread any iterable objects using * operator python
# ! And to spread keyword arguments we need to use ** operator

dict_my_list = dict(my_list)

# new_dict = dict(a="e", b="f", d=12, *my_list)

second_dict = dict(b="f", d=12, **dict_my_list)

# print(new_dict)
# print(second_dict)


# ? int()

y = int(34.58)
x = int("40")
# print(x, type(x))
# print(y)

# ? max()

a_list = [15, 155, 142, 639, 778]
b_list = ["apple", "banana", "pineapple", "cherry", "date"]
# print(max(b_list, key=len))

# ? min()

ab_list = [15, 155, 142, 639, 778]
bb_list = ["apple", "banana", "pineapple", "cherry", "date"]
# print(min(bb_list, key=len))


# ? sum()

numbers = [1, 2, 3, 4, 5]
mysum = sum(
    numbers, start=20
)  # ! we can pass start argument to this function ex. start = 10
# print(mysum)

# ? zip()
# * The zip() function is used to combine two or more iterables into a single iterable.

colors = ["Yellow", "Blue", "Orange"]
hex_values = ["#FFFF00", "#0000FF", "#FFA500"]

color_with_codes = dict(zip(colors, hex_values))
print(color_with_codes)


# ? map()

my_words = ["apple", "banana", "pineapple", "cherry", "date"]

capitalized_words = list(map(lambda word: word.capitalize(), my_words))

# print(capitalized_words)

# ? filter()

apple_list = list(filter(lambda item: item.startswith("a"), my_words))[0]

# print(apple_list)


list_of_dict = [
    {"name": "Aakash", "age": 19},
    {"name": "Bhavesh", "age": 16},
    {"name": "Harsh", "age": 21},
    {"name": "Tarun", "age": 22},
]

tarun_dict = list(filter(lambda item: item["name"] == "Tarun", list_of_dict))[0]

# print(tarun_dict)


# ? sorted()

x_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
y_list = sorted(x_list)
print(y_list)

# ? enumerate()

fruits = ["apple", "banana", "kiwi", "mango"]

# ! we can also start from another sequence start = 100
for index, fruit in enumerate(fruits, start=100):
    print(index, fruit)

# ? reversed()

# print(list(reversed(y_list)))

# * sorted but in reverse

print(sorted(x_list, reverse=True))
