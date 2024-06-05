class Calculator:

    def add(self, x: int, y: int):  # type: ignore
        return x + y

    def add(self, x: float, y: float):  # type: ignore
        return x + y

    def add(self, x: str, y: str):  # type: ignore
        return x + y

    def add(self, x: int, y: int, z: int):
        return x + y + z


calc = Calculator()

# ! Automatic type casting
# ? print(calc.add(int("15"), int("14"), 10.4))  # type: ignore
