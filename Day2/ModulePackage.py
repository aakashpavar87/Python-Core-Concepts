from collections import OrderedDict
import heroes
from prettytable import PrettyTable
from faker import Faker
import random
from art import ball

def table_printer():
    table = PrettyTable()

    table.field_names = ["Name", "Type","Main Attack","Next Form","Evo Stone"]

    # List 1
    pokemon1 = ["Pikachu", "Electric", "Thunderbolt", "Raichu", "Thunder Stone"]

    # List 2
    pokemon2 = ["Eevee", "Fire", "Flamethrower", "Flareon", "Fire Stone"]

    # List 3
    pokemon3 = ["Poliwhirl", "Water", "Bubble Beam", "Poliwrath", "Water Stone"]

    # List 4
    pokemon4 = ["Gloom", "Grass/Poison", "Petal Dance", "Vileplume", "Leaf Stone"]

    # List 5
    pokemon5 = ["Clefairy", "Fairy", "Moonblast", "Clefable", "Moon Stone"]

    table.add_rows([
        pokemon1,
        pokemon2,
        pokemon3,
        pokemon4,
        pokemon5,
    ])

    table.align = "l"

    print(table.get_string())

def random_hero_generator():
    print(heroes.genarr(10))

def random_fake_data_generator():
    fake = Faker("en_IN")
    for _ in range(10):
        fake_data = {
            'name': fake.name(),
            'address':fake.address(),
            'text':fake.sentence()
        }
        print(fake_data)        
        
# random_fake_data_generator()

def random_coin_flipper():
    '''This function flips coin and plays toss with you'''
    print(ball)
    computer = random.randint(0,1)
    user = input("Choose one Head (H) or Tails (T) : ")
    if((computer == 0 and user == "H") or (computer == 1 and user == "T")):
        print("Yay you won the toss.")
        user_choice = input("Do you want to play YES (Y) or NO (N) : ")
        if user_choice == "Y":
            random_coin_flipper()
        else:
            return
    else:
        print("You lose !!!")
        return

random_coin_flipper()
    
    
