import math


def sqrt(x):
    try:
        print(math.sqrt(x))
    except TypeError:
        print("Invalid input.")

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

# division
try:
    division = float(number1) / float(number2)  # error
    print(f"Division = {division}")  #
except ZeroDivisionError:  # as specific
    print("You can not divide by zero")
else:
    print("Done with division.")

arr = [1, 2, 3]
try:
    print(arr[5])
except IndexError:
    print("wrong index")  # do nothing, fail silently

table = {"sachin": 1}
try:
    print(table['Sachin'])
except KeyError:
    pass  # do nothing

# it is good practice to report the errors
# ignore the errors

num = 81
sqrt(num)

num = "string"
sqrt(num)

#
# Testing your code
# write a python program to test other program : automated testing/unit testing
#