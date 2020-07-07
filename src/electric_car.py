
from car import Car

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # instance variable, composition, one object
                                 #  contains another object

    def replace_battery(self, new_battery):
        print("Replacing the battery ...")
        self.battery = new_battery

    # method override: change the implementation
    def fill_gas_tank(self):
        print(f"Electric car does not have a gas tank.")


class Battery:
    """model a battery for an electric car"""

    def __init__(self, battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 200:
            print("upgrading the battery ...")
            self.battery_size = 200


# my_tesla = ElectricCar("Tesla", "Model 3", 2019)
#
# # my_tesla.get_description()  # this is defined in a parent class
#
# my_tesla.battery.describe_battery()  # method chaining
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()





