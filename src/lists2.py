
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# sort a list by alphabetical order
# cars.sort()
# print(cars)
#
# cars.sort(reverse=True) # reverse order sort
# print(cars)

print(sorted(cars))  # temporarily sort a list
print(cars)

cars.reverse()
print(cars)

print(len(cars))

# print(cars[4])  # exceptions

# comment
for car in cars:
    print(car.title())  # 4 spaces of indentation

for value in range(1, 1):  # in operator always works with list
    print(value)

for number in [1, 2, 4, 2]:  #
    print(number)

numbers = [11, 232, 44, 0, 2, 5]
smallest_number = min(numbers)
print(smallest_number)
biggest_number = max(numbers)
print(biggest_number)
print("sum of all numbers:", sum(numbers))

# List comprehensions: allows you to generate a list using some code

# list of squares for numbers: 1 - 10
# ** exponent

print("--------")
for x in range(1, 11):
    print(x**2)
print("--------")

squares = [x**2 for x in range(1, 11)]
print("squares of 1 - 10: ", squares)

cubes = [x**3 for x in range(1, 11)]
print("cubes of 1 - 10: ", cubes)

# slice of list (part of the list)
print("Cubes of first 5 numbers: ", cubes[0:5])  # 0, 1, 2, 3, 4
print("Cubes of numbers from 2 - 4: ", cubes[1:4])  # 0, 1, 2, 3, 4

start = 0
end = 6
print(cubes[:end])  # slice 0 --> 5 end index non-inclusive
print(cubes[4:])  # slice 0 --> 5 end index non-inclusive

print(cubes[:])

# slice of last 3 numbers in the list
print(cubes[-3:])
print(cubes[-3:-1])  #


for number in cubes[4:8]:  # list slice from 4th to 7th item
    print(number)

squares2 = squares
print(squares)
squares[0] = 9999
print("squares:", squares)
print("squares2:", squares2)

squares3 = squares[:]  # new slice
print(squares3)
squares[0] = 1111
print(squares3)
squares[5] = 42942940
print(squares)

# lists in python are mutable(changeable): that means you can change/modify the values

# tuple -- immutable <-- you cannot change values

x = (2, 4)  # using a round bracket, it is a tuple

print(x)
print(x[0])  # accessing the value

for i in x:
    print(i)

x = (3, 9)   # types are dynamic

