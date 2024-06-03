def make_intro(name):
    print(f"Hello {name}")


# make_intro("Aakash")

# ! Function with *args


# ? When we want to pass multiple positional arguments we pass *args
def multiple_args(name, *skills):
    print(f"{name} has skills that are given below ")
    for skill in skills:
        print(skill, end=" ")
    print()


def keyword_args(**kwargs):
    for key, item in kwargs.items():
        if item is not int:
            print(f"{key} : {item}")
        else:
            print(f"{key} : {str(item)}")


# keyword_args(age=16, weight=15.4, language_known="python, php, javascript")


def required_params(n2, *n1):
    print(f"First : {n1} Second : {n2}")


# try:
#     required_params(23, 55, 74, 88)
# except:
#     print("Functions needs two params...")


def default_args(n1, n2=100):
    print(f"First : {n1}, Second : {n2}")


# default_args(23)


# multiple_args("Aakash", "coding", "listening", "reading", "cooking")

# ! lambda functions
# ? Syntax :lambda1 = lambda argument1, argument2 : operation on both arguments

# print(lambda1(15, 25))


def filter_even_numbers(*numbers):
    return [num for num in numbers if num % 2 == 0]


# print(filter_even_numbers(15, 14, 62, 31, 74, 73, 86))


def sum_all_numbers(*numbers):
    total = sum(numbers)
    return total


# print(sum_all_numbers(14, 14, 14, 14, 14))


# ? Merge Dictionaries Merge Dictionaries:
# ? Write a function merge_dicts(*dicts) that takes any number of dictionaries and merges them into a single dictionary. If there are duplicate keys, the value from the last dictionary should be used.


# ? Update method of dictionary checks for key if key is exists it will overwrite with current value
def merge_dict(*dicts):
    """This function merges dictionaries and checks for duplicate keys."""
    merged_dict = {}
    for dictionary in dicts:
        merged_dict.update(dictionary)
    return merged_dict


merged_dictionaries = merge_dict(
    {"name": "Aakash", "color": "green", 2: 568}, {"name": "BGMI", 2: "Mango"}
)
# print(merged_dictionaries)


# ! Flexible function caller


def flexible_caller(func, *args, **kwargs):
    func(args, kwargs)


def printval(arg1=(), arg2={}):
    print(arg1)
    print(arg2)


def merger(arg1, arg2):

    joined_text = " ".join(str(item) for item in arg1)
    joined_list = [[key, item] for key, item in arg2.items()]

    print(joined_text)
    print(joined_list)


# flexible_caller(
#     printval, 25, 54, "Name", 58, 12.4, name="Aakash", color="gray", language="python"
# )

# flexible_caller(merger, 34, 44, 23, 22, "Harsh", "Jaimin", fruit="banana", game="BGMI")


# ? Dynamic Function Generator:
# ? Write a function create_adder(*args) that returns another function which adds all the *args to its own arguments when called


def create_adder(*args):

    def add_values(value):
        for v in args:
            value += v
        return value

    return add_values


add4 = create_adder(4, 5)

# print(add4(16))


# ! Lambda Functions practice

addTwoNum = lambda num1, num2: num1 + num2

checkIsEven = lambda num1: num1 % 2 == 0


print(checkIsEven(12))
