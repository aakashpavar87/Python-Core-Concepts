first_dict = {12: "Aakash"}

# print(first_dict)

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

# print(person["age"])

# print(person.get("last_name"))

# ! Adding element in dict

person["game"] = ["velorant", "Clash Of Clains", "BGMI"]

person["game"].append("Free Fire")

person["is_married"] = False
# print(person.get("game"))

# ! Removing element from dictionary

# * pop(key): removes the item with the specified key name:
# * popitem(): removes the last item
# * del: removes an item with specified key name

# person.pop("country")

# person.popitem()

# * del person["skills"]
# * for value in pers

# ? dict.values() it will give list of all values in dict
# ? dict.keys() it will give list of all keys in dict
# ? The fromkeys() method returns a dictionary with the specified keys and the specified value.
print(dict.fromkeys(["age", "name"], "N/A"))

# ! Iterating from each value in dictionary by .items() method

# ? for key, value in person.items():
# ?    print(f"{key} : {value}")

x = ("key1", "key2", "key3")
y = 0

thisdict = dict.fromkeys(x, y)

# print(thisdict)

# ? copy method creates another object of dictionary and then assigns new memory address
thatdict = thisdict.copy()
that2 = thatdict

print(id(that2))
print(id(thatdict))

thatdict["key1"] = "First"
that2["key2"] = "Second"

# ? id fn is used to find address of one variable
print(thatdict)
print(that2)

# ! Same address problem arrived here and in above code
print(id(thatdict))
print(id(that2))
