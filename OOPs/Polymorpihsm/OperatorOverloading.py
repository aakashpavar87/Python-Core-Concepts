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

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"


v1 = Vector(12, 11)

v2 = Vector(14, 12)

v3 = v1 + v2

v4 = v2 - v1

v5 = Vector(50, 5)

v6 = Vector(100, 10)

v7 = v6 / v5  # type: ignore

print(v3)

print(v4)

print(v7)
