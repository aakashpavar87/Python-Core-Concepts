from functools import reduce

countries = [
    "Estonia",
    "Finland",
    "Sweden",
    "Denmark",
    "China",
    "Japan",
    "Norway",
    "Iceland",
]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

upper_country = list(map(lambda c: c.upper(), countries))
upper_names = list(map(lambda c: c.upper(), names))
square_num = list(map(lambda n: n**2, numbers))
land_containing_countries = list(filter(lambda c: c.endswith("land"), countries))
e_starting_countries = list(filter(lambda c: c.startswith("E"), countries))
length_having_six_countries = list(filter(lambda c: len(c) == 6, countries))
length_having_six_or_more_countries = list(filter(lambda c: len(c) <= 6, countries))

print(f"{upper_country=}")
print(f"{upper_names=}")
print(f"{square_num=}")
print(f"{land_containing_countries=}")
print(f"{e_starting_countries=}")
print(f"{length_having_six_countries=}")
print(f"{length_having_six_or_more_countries=}")


sum_of_square_of_even = reduce(
    lambda x, y: x + y,
    list(filter(lambda n: n % 2 == 0, list(map(lambda n: n**2, numbers)))),
)
print(f"{sum_of_square_of_even=}")


def get_string_list(seq):
    return list(filter(lambda item: type(item) == "str", seq))


my_list = ["apple", 15, "banana", 54.2, [12, 33], {"name": "Aakash"}]
print(get_string_list(my_list))
