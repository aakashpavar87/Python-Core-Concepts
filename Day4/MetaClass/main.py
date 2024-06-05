class Test:
    pass


t = Test()
t.de = "Hell"
print(t.de)


class Me:
    name = "Aakash"


He = type("He", (Me,), {"him": "Hahaha", "fun": "nothing"})

print(He.him)  # type: ignore
print(He.name)
print(He.fun)


Test1 = type("Test1", (), {})

print(type(Test1))
print(type(Test))
