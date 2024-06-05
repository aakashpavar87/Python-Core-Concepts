from abc import ABC, abstractmethod


class Game(ABC):
    @abstractmethod
    def create_player(self, name, ability, strength):
        pass


class Mario(Game):
    def create_player(self, name, ability, strength):
        return {"name": name, "ability": ability, "strength": strength}


class Contra(Game):
    def create_player(self, name, ability, strength):
        return {"name": name, "ability": ability, "strength": strength}


contra_abilities = ["jump", "sit", "swimm", "fire"]

mario_abilities = ["jump", "sit", "swimm"]

m1 = Mario()
print(m1.create_player("Mr. Mario", mario_abilities, "running"))

c1 = Contra()
print(c1.create_player("Mr. Contra", contra_abilities, "killing"))
