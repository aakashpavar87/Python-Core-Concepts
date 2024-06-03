my_global_name = "Aakash"


# ! We have two scopes in python first is global scope and second local scope which is inside any function and method of class

# ! We have two keywords for accessing global and local varibles
# * 1. global
# * 2. nonlocal


def fun():
    # ? updating global variables
    # global my_global_name
    my_global_name = "Kris"

    def another_fun():
        nonlocal my_global_name
        my_global_name = "Kris the Kanhaiya"

    another_fun()
    print("In Fn : " + my_global_name)


fun()


print("Out side Fn : " + my_global_name)
