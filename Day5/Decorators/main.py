import time


def logger(func):
    def wrapper(*args, **kwargs):
        print("Before Calling fn : ", time.time())
        # time.sleep()
        rv = func(*args, **kwargs)
        print("After Calling fn : ", time.time())
        return rv

    return wrapper


@logger
def myfun(x, y):
    return x + y


@logger
def hisFun():
    print("Just a normal function")


# ! We can do this without using decorator syntax
# ? myfun = logger(myfun)
# ? hisFun = logger(hisFun)

print(myfun(12, 12))
hisFun()
