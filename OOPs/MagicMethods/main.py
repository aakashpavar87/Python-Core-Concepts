from datetime import datetime

today = datetime.now()

# print(f"{today = !s}")

age = 12

# print(repr(age))

# print(f"{today = !r}")


class Book:

    book_name: str = ""
    book_price: int = 0

    def __init__(self, book_name, book_price):
        self.book_name = book_name
        self.book_price = book_price

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.book_name} of price {self.book_price})"

    def __str__(self):
        return self.book_name


book1 = Book("Life Of PI", 25800)

book2 = Book("Secret Of Money", 12000)

# print(book1)
# print(book1.__repr__())

# print(book2)
# print(book2.__repr__())


# ! __new__() method for instance creation


class Storage(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit  # type: ignore
        return instance


disk = Storage(10240, "GB")

print(disk)

print(disk.unit)  # type: ignore


class Vector:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):  # type: ignore
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # type: ignore
        return Vector(self.x - other.x, self.y - self.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if other.x == 0 or other.y == 0:
            return Vector(float("inf"), float("inf"))  # type: ignore
        return Vector(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        if other.x == 0 or other.y == 0:
            return Vector(float("inf"), float("inf"))  # type: ignore
        return Vector(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Vector(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return Vector(self.x**other.x, self.y**other.y)

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"


v1 = Vector(12, 34)
v2 = Vector(6, 16)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print(v1 // v2)
print(v1**v2)
