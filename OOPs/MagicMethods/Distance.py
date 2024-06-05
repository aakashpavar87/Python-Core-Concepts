class Distance:
    _multiples = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1_000,
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit.lower()

    def to_meter(self):
        return self.value * type(self)._multiples[self.unit]

    def __isUnitSame(self, other):
        if not self.unit == other.unit:
            raise TypeError(
                "unsupported operand for +: " f"'{self.unit}' and '{other.unit}'"
            )

    def __add__(self, other):
        self.__isUnitSame(other)
        return self._compute(other, "+")

    def __sub__(self, other):
        self.__isUnitSame(other)
        return self._compute(other, "-")

    def _compute(self, other, operator):
        operation = eval(f"{self.to_meter()} {operator} {other.to_meter()}")
        cls = type(self)
        return cls(operation / cls._multiples[self.unit], self.unit)

    def __str__(self):
        return f"{self.value} {self.unit}"


try:
    d1 = Distance(100, "cm")
    d2 = Distance(50, "km")
    print(d2 - d1)
except Exception as exc:
    print(exc)
