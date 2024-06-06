def linux_interaction():
    import sys

    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")


# ! Handling exception in function definition
def take_number_and_add(num):
    try:
        num2 = int(input("Give me Another number : "))
        return num + num2
    except KeyboardInterrupt as error:
        print(error)
        take_number_and_add(num)


try:
    linux_interaction()
    number = 5
    res = take_number_and_add(number)
    # assert number > 10, print(f"Give bigger number : {number=} ")
    # print(aakash)
    print(number)
except NameError as error:
    print(error)
    print("Define variable which you have used")
except RuntimeError:
    print("Linux wont execute on windows")
# except KeyboardInterrupt as error:
#     print(error)
except TypeError as error:
    print(error)
    print("please give correct type of data")
except AssertionError:
    pass
except Exception as error:
    print(error)
    print("general exception")
else:
    print(res)
    print("Programm has finished execution without error")
finally:
    print("I am Finally block I will run always")
