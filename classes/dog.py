class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is now roll_over")


my_dog = Dog('Bobby', 6)
print(f"My dog name is {my_dog.name} and he {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()
