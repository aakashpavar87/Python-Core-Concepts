food_stuff_tp = ("burger", "pizza", "hot dog", "noodles", "paasta")
food_stuff_lst = list(food_stuff_tp)
print(type(food_stuff_lst))

fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_vegetables = list(fruits + vegetables)

print(fruits_and_vegetables)
print(type(fruits_and_vegetables))

# [print(x) for x in fruits_and_vegetables]

# * Deleting tuppples with del keyword

del fruits
