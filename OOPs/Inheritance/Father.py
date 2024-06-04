class Father:
    __name = "Mister Dad"

    def __init__(self) -> None:
        self.salary = 150000

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.salary

    def set_name(self, new_name):
        self.__name = new_name


mr_smith = Father()

mr_smith.set_name("Mr Smith")

print(mr_smith.get_name())
