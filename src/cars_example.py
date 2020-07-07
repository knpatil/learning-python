
#from car import Car
#from electric_car import ElectricCar, Battery

#from electric_car import *
from electric_car import ElectricCar as EC # creating an alias
from electric_car import Battery as B
from car import Car

my_new_car = EC("Chevy Volt", "Volt 4", 2020)
my_petrol_car = Car("Toyota", "Camry", 2019)

my_new_car.get_description()
my_petrol_car.get_description()
my_new_car.battery.describe_battery()

new_battery = B(500)

my_new_car.replace_battery(new_battery)

my_new_car.battery.describe_battery()

# styling classes
# Class name always starts with Uppercase letter, CamelCase pattern for
# multiple words in class name





