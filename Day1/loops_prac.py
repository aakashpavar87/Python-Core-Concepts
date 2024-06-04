import random
fruits = ['apple', 'banana', 'grapes', 'mango']

words = "This is a long sentence written by Aakash Pavar".split(" ", maxsplit=4)
capitalized_fruits = []
for i in fruits:
    capitalized_fruits.append(i.upper())
# print(capitalized_fruits)
# print(words)

is_game_on = True

while is_game_on:
    choice = str(input("Enter your choice Heads (H) or Tails (T) : "))
    computer_choice = random.choice(["H", "T"])
    if choice == computer_choice:
        print("You win ! ")
    else :
        print(f"Computer \'s choice {computer_choice}")
        print("You loss the Toss :( ")
    if str(input("Do you want to play again ? Y/N ")) == "N":
        is_game_on = False
    