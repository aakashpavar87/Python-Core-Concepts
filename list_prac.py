import random
fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes', {'name': 'Aakash'}]

a,b,c,*d, name_dict=fruits

print(a)
print(b)
print(c)
print(d)
print(name_dict)

print(fruits[-3:-1])

mydict = {'name': 'Aakash'}

print(mydict in fruits)

# ? Appending items to list and Inserting items at specific index of list

numbers = [12,22,33,44,554,56]
numbers.append("New Number")
# print(numbers)


numbers.insert(-3, "Inserted Item")

# print(numbers)

# ? Removing item from list

numbers.remove('Inserted Item')
print(numbers)

# ? Poping out top elements of list last element

print(numbers.pop(2))

numbers.insert(1, [12,34,66])

print(numbers)

cricket_items = ["bat", "ball", "stumps" ,"bails"]

valleyball_items = ["ball", "net"]

playing_items = cricket_items+valleyball_items

print(playing_items)

# ? Finding index of one element

bails_index = cricket_items.index("bails")

print(f"Index of BAils : {bails_index}")

print(f"Count of ball in playing items : {playing_items.count('ball')}")

cricket_items.reverse()

print(cricket_items)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack_tech = (front_end + back_end)

print(full_stack_tech)

full_stack_tech.insert(5, 'Python')
full_stack_tech.insert(6, 'SQL')

print(full_stack_tech)

full_stack_tech.sort()

print(f"Sorted Full Stack List : {full_stack_tech}")


# ? sorted function is used for sorting by different parameters or factors

# ! Example here we can pass any function which takes one parameter.

a = ("Jjnkfwr", "Jane", "Jtnh")
# * x = sorted(a, key=len)
x = sorted(a, key=len)
print(x)







