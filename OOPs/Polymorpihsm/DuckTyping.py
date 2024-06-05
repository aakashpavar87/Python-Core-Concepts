class Duck:
    def make_sound(self):
        print("Quack Quack")


class Goose:
    def make_sound(self):
        print("Honk Honk")


def make_animal_sound(animal):
    animal.make_sound()


duck = Duck()

goose = Goose()

make_animal_sound(duck)

make_animal_sound(goose)
