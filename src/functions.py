def greet_user():  # function definition
    """Display a simple greeting."""  # docstring, describe what the function should do
    print("Hello!")


greet_user()  # function call


# function naming conventions, lowercase, _ (underscore)


def greet_user2(username):  # receiving a parameter
    """Display a simple greeting."""
    print(f"Hello, {username}")


greet_user2("George")  # passing an argument


def describe_pet(animal_type, pet_name):  # positional parameters
    """"Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name}.")


describe_pet("Dog", "Tommy")  # correct order
describe_pet("Tommy", "Dog")  # wrong order
describe_pet("Cat", "Minnie")
describe_pet("Mouse", "Mickey")

# call the function using keyword argument
describe_pet(animal_type="Tiger", pet_name="Scott")
describe_pet(pet_name="Scott", animal_type="Tiger")  # different order is ok


# Default values
def describe_pet2(pet_name, animal_type="Dog"):  # default value
    """"Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name}.")


describe_pet2("Tommy")  # second argument is not needed, it has default value
describe_pet2(pet_name="tommy")  # keyword argument
describe_pet2("Minnie", "Cat")
describe_pet2(pet_name="Mickey", animal_type="Mouse")
describe_pet2(animal_type="Mouse", pet_name="Mickey")


# return values: return statement, you don't need to define beforehand
def get_formatted_name(first_name, last_name):
    """"Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name


cricketer = get_formatted_name("Sachin", "Tendulkar")
print(f"\nFull name is '{cricketer}'")


def get_formatted_name2(first_name, last_name, middle_name=''):
    """"Return a full name, neatly formatted"""

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name


cricketer2 = get_formatted_name2("Sachin", "Tendulkar")
print(f"\nFull name is '{cricketer2}'")

cricketer3 = get_formatted_name2("Sachin", "Tendulkar", "Ramesh")
print(f"\nFull name is '{cricketer3}'")


# returning a dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {"first_name": first_name, "last_name": last_name}
    if age:
        person["age"] = age
    return person


dancer = build_person("Michael", "Jackson")
print(dancer)

dancer2 = build_person("Michael", "Jackson", 50)
print(dancer2)


# while True:
#     print("\n Please tell me your name: ")
#     first_name = input("First name: ")
#     last_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(first_name, last_name)
#     print(f"Hello, {formatted_name}")

# pass dictionary as a parameter
# pass list as a parameter, dict, list, string, number

def display(list_of_models):
    """print the models from the list"""
    for model in list_of_models:
        print(model)
    list_of_models.append("BMW")


car_models = ["Honda", "Toyota", "Audi"]
print("Car Models:", car_models)

display(car_models)  # passing a reference, in python, everything is object

print("Car Models:", car_models)

print("-" * 80)

# not to modify original list
car_models2 = ["Honda", "Toyota", "Audi"]
print("Car Models:", car_models2)
display(car_models2[:])  # create a list slice (copy)
print("Car Models:", car_models2)


# variable number of arguments
def make_pizza(size, *toppings):  # arbitrary arguments
    """Print the list of toppings that have been requested"""
    print(f"Pizza Size: {size}")
    print(f"\t with toppings: {toppings}")

    print("type=", type(toppings))  # immutable list -> tuple, list of values


make_pizza("Small", "Olives")
make_pizza("Medium", "Olives", "Onion", "Tomato", "Paneer")
make_pizza("Small", "Olives", "Tomato", "Paneer")
make_pizza("Large", "Olives", "Tomato", "Paneer")


#
# arbitrary keyword arguments
#
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""

    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info


user_profile = build_profile('albert', 'einstein', location='Lake Tahoe', field='physics', job='scientist')
print("\n\nUser Profile: ", user_profile)

user_profile = build_profile('isac', 'newton')
print("\n\nUser Profile: ", user_profile)


def make_car(model, car_type, **car_info):
    car_info['model'] = model
    car_info['type'] = car_type
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print("Car Details: ", car)

#
# Modules in python: collection of functions stored in some file
# organizing code
# all the related function in one module: math.py ->> sin, cos, tan
#