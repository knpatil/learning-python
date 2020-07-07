class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # odometer
        self.odometer_reading = 0
        self.color = "red"

    def get_description(self):
        print("My car details: ")
        print(f"\t Make: {self.make}")
        print(f"\t Model: {self.model}")
        print(f"\t Year: {self.year}")
        print(f"\t Color: {self.color}")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def drive_car(self, kms):
        print(f"Driving this car by {kms} kilometers")
        self.odometer_reading += kms

    def paint_car(self, color):
        print(f"Painting the car with color {color}")
        self.color = color

    def fill_gas_tank(self):
        print(f"Filling gas tank in this model {self.model}")

# my_new_car = Car("Audi", 'A4', 2020)
# my_new_car.get_description()
# my_new_car.read_odometer()
#
# my_new_car.drive_car(10)
# my_new_car.read_odometer()
#
# my_new_car.drive_car(400)
# my_new_car.read_odometer()
#
# my_new_car.drive_car(200)
# my_new_car.read_odometer()
#
# my_new_car.paint_car("Blue")
# my_new_car.get_description()
