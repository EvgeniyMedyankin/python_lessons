from dog import *
from car import Car, ElectricCar as EC
from time import sleep

my_dog = Dog('Bobby', 6)
print(f"My dog name is {my_dog.name} and he {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()

sleep(5)

print("#----------------#")

my_new_car = Car('audi', 'A4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(45)
my_new_car.read_odometer()

my_new_car.update_odometer(15)
my_new_car.read_odometer()

my_new_car.increment_odometer(15)
my_new_car.read_odometer()

my_tesla = EC('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
