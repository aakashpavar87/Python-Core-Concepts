class Meta(type):

    def __new__(self, class_name, bases, attrs):  # type: ignore
        print(attrs)
        new_attrs = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                new_attrs[key] = value
            else:
                new_attrs[key.upper()] = value
        print(new_attrs)
        return type(class_name, bases, new_attrs)


class Bird(metaclass=Meta):

    # ! If we will not provide class attributes here than meta class would not recognise them

    name = ""
    species = ""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def say_hello(self):
        print(f"Hello from {self.name}")


sparrow = Bird("piko", "sparrow")

sparrow.SAY_HELLO()  # type: ignore
