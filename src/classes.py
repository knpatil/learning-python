# in object oriented programming, you write classes
# Classes: represent real-world things and situations
# you create objects
#
# class : define some general behavior
# object -- object instantiation
#
# Pet Dog
#
#    What does this class (dogs) have in general? Properties they have
#         name
#         age
#
#    What can Dogs do? General Behavior
#         sit
#         roll over
#         eat
#         catch the ball
#
# Vehicles
#  In general
#      Properties: model, color, make (instance variables)
#      Behaviors: accelerate, mileage, turn right (method)
#
# Name of class starts with uppercase letter
#

class Dog:
    """A simple model class for Dog"""

    # constructor
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over"""
        print(f"{self.name} of age {self.age} is now rolling over")


# write different code
# self is reference to the object itself

# create an instance of class
my_dog = Dog('Willie', 7) # notice we are passing any value for self

# call the methods
my_dog.sit()  # call method sit
my_dog.roll_over() # call method roll over

# accessing attributes
print(f"My dog's name is {my_dog.name} and it's age is {my_dog.age}")

# create another instance/object
another_dog = Dog('Tommy', 3)
print(f"My dog's name is {another_dog.name} and it's age is {another_dog.age}")










