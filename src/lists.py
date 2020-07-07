
# built-in data structure

# collection

# there are 4 built-in data structure

# List: ordered collection of objects
cities = []
print(cities)
cities = ["San Jose", "Las Vegas", "Mumbai"] # 3 objects
print(cities)

cities.append('Pune')
cities.append('Dhule')

# print(cities)
#
# print("city: ", cities[2])
#
cities.remove("Dhule")
# print("last item: ", cities[-1])


for x in cities:
    print(x)


for index, city in enumerate(cities):
    print(cities[index])

# grow a list at runtime using append
# remove an item : remove

print(len(cities))

if "Pune" in cities:
    print("pune is there!")

if "Delhi" not in cities:
    cities.append("Delhi")

print(cities)
del cities[3]

print(cities)

# Stack data structure

cities.append("Nashik")  # push
print(cities)

last_item = cities.pop()
print(last_item)

cities2 = ["A", "B", "C"]

cities.extend(["a", "b", "c"]) # extend the list with new

print(cities)

cities.insert(4, "Lake Tahoe")
print(cities)


