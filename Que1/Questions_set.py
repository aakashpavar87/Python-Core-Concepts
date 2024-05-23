it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.add("Twitter")
print(len(it_companies))

it_companies.update(["Adobe", "Netflix", "Meta"])
print(it_companies)


# it_companies.remove("Meta")

# ! discard method don't throws error if element is not found but remove method throws error if element not found
it_companies.discard("Meta")
print(it_companies)


# print(A)
# print(B)

# print(B.issuperset(A))

# print(A.issubset(B))


# print(A.intersection(B))

# print(A.isdisjoint(B))

B.union(A)

# print(B)

A.union(B)

print(A)

print(A.symmetric_difference(B))

del A, B

list = "I am a teacher and I love to inspire and teach people.".split(" ")

list_set = set(list)
print(len(list_set))
