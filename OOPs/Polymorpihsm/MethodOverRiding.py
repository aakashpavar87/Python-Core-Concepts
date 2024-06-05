class Car:
    def start(self):
        print("Car started with power ...")


class SuperCar(Car):

    # ! Overridden Method
    def start(self):
        print("Car started with Ultra Power")


SuperCar().start()

Car().start()
