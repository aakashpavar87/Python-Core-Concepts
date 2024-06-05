class Car:
    car_engine = 10000
    car_speed = 120
    no_of_cars = 0

    def __init__(self, brand, model):
        # private variable
        Car.no_of_cars += 1
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    @classmethod
    def get_car_speed(cls):
        return cls.car_speed

    @classmethod
    def increase_car_speed(cls, increment):
        cls.car_speed += increment

    @classmethod
    def improve_engine(cls, improvment):
        cls.car_engine += improvment

    @staticmethod
    def general_desc():
        """This method gives universal description to car"""
        print("Cars are amazing")

    @staticmethod
    def get_engine_info():
        print(f"{Car.car_engine} Horse Power")

    def get_fuel_info(self):
        print("Petrol and Diesel")

    @property
    def model(self):
        return self.__model

    def __str__(self) -> str:
        return f"Car Brand : {self.__brand} Car Model : {self.__model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def charge_battery(self):
        print("Battery is charged")

    def get_fuel_info(self):
        print("Electricity")

    def get_battery_info(self):
        print(f"This battery has {self.battery} capacity.")


my_car = Car("TOYOTO", "Corolla")
print(my_car)
tata_thar = Car("TATA", "THAR")
tata_thar.get_fuel_info()
electric_thar = ElectricCar("TATA", "THAR", "80 kwh")
electric_thar.get_fuel_info()
electric_thar.get_battery_info()

print(Car.no_of_cars)
