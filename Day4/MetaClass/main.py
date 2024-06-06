class Test:
    pass


t = Test()
t.de = "Hell"  # type: ignore
print(t.de)  # type: ignore


class Me:
    name = "Aakash"


He = type("He", (Me,), {"him": "Hahaha", "fun": "nothing"})


def justfun(self):
    print("Just for fun")


print(He.him)  # type: ignore
print(He.name)
print(He.fun)  # type: ignore


Test1 = type("Test1", (He,), {"justfun": justfun})

newtest = Test1()  # type: ignore
newtest.justfun()  # type: ignore
