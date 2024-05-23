# ! Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

fruits = ["banana", "orange", "mango", "lemon"]

set1 = set(fruits)

# print(type(set1))

# ? Once a set is created we cannot change any items and we can also add additional items.

set1.add("grapes")

# print(set1)

set1.update(["12", 98])

# print(set1)

# set1.pop()
st1 = {"item1", "item2", "item3", "item4", "item5", "item6"}
st2 = {"item5", "item6", "item7", "item2", "item8"}
st3 = {"item5", "item6"}
# ! st3 = st1.union(st2) it is used to find union of two sets
# ? This method is used to insert more than one elements in set
# st1.update(st2)

# ! Intersections in two sets
# * print(st1.intersection(st2))

# ! Superset or Subset Checking

# * print(st2.issuperset(st3))

# * print(st3.issubset(st2))

# * print(st1.issuperset(st3))


print(st1.difference(st2))
print(st2.difference(st1))


print(f"Symmetric Difference b/w st1 and st2 : {st1.symmetric_difference(st2)}")

print(st2.difference(st3))

# ? difference in context of st3
print(st3.difference(st2))

print(st1.difference(st3))


python = {"p", "y", "t", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(
    python.difference(dragon)
)  # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))  # {'d', 'r', 'a', 'g'}

print(python.symmetric_difference(dragon))

# ! discard method don't throws error if element is not found but remove method throws error if element not found
# * it_companies.discard("Meta")
# * print(it_companies)

seta = {1, 2}
setb = {1, 4}

print(seta.difference(setb))
print(setb.difference(seta))
print(setb.symmetric_difference(seta))
