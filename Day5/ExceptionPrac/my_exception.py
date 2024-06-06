class MyException(ValueError):
    pass


def take_age(x: str = "") -> int:
    age = int(input("Enter your age : "))
    try:
        if age < 16:
            raise MyException("You can not continue from now.")
        elif age > 110:
            raise MyException("You are too old to continue.")
    except MyException as error:
        print(error)
        return 0
    else:
        print("You can give driving test")
        print(x)
        return age


try:
    take_age()
    # print(num)
    squares_of_two_nums = [(f**2, f**3) for f in range(1, 11)]
    print(squares_of_two_nums)
except Exception as error:
    print("Error of outer try")
    print(error)
else:
    print(take_age.__annotations__)


if __name__ == "main":
    pass
