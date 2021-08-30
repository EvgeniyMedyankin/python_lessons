print("# --------------- #")

a = "Text string"
print(a)
print(a.upper())
print(a.lower())
a = a.lower()
print(a.islower())

print("# --------------- #")

first_name = "evgeniy"
last_name = "mediankin"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}"
print(message)
summa = 2 + 3
print(summa)
universe_age = 14_000_000_000
print(universe_age)
x, y, z = 0, 0, 0
print(x, y, z)
MAX_CONNECTIONS = 1000
print(MAX_CONNECTIONS)
MAX_CONNECTIONS = 3000
print(MAX_CONNECTIONS)

print("# --------------- #")

auto = ["trek", "redline", "specialize"]
print(auto[0])
print(auto[-1])
auto.append("skoda")
print(auto)
auto.insert(1, "honda")
print(auto)
del auto[0]
print(auto)

print("# --------------- #")

motorcycles = ["honda", "ducati", "bmw", "yamaha"]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print("# --------------- #")

print(motorcycles)
to_expensive = "ducati"
motorcycles.remove(to_expensive)
print(motorcycles)
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(len(cars))
print(len(cars[0]))

print("# --------------- #")

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

for value in range(1, 10):
    print(value)

print("# --------------- #")

numbers = list(range(1, 10))
print(numbers)

numbers = list(range(1, 10, 2))
print(numbers)

print("# --------------- #")

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

print("# --------------- #")

digits = range(1, 10)
print(min(digits))
print(max(digits))
print(sum(digits))

print("# --------------- #")

players = ["charles", "anna", " martina", "nikolai", "eli"]
print(players)
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:3])
print(players[:])

print("# ------Кортежи--------- #")

dimensions = [200, 50]
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 250
print(dimensions[0])

print("# --------------- #")

age = 55
if age <= 25 or age == 30:
    print("good!")

request_toppings = ["mushrooms", "onions", "pineapple"]

print('mushrooms' in request_toppings)

age = 22

if age == 18:
    print("Age 18")
elif age == 17:
    print("Age 17")
else:
    print("Age default")

rr = "ss2233"
print(rr)

print("# --------------- #")

alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)
print(f"Alien color is {alien_0['color']}")
alien_0['color'] = 'red'
print(f"Alien color is {alien_0['color']}")
del alien_0['points']
print(alien_0)
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value')
print(point_value)

for key, value in alien_0.items():
    print(f"\n Key: {key}")
    print(f" Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'evgeniy': 'js',
}

print("\n")

for lang in favorite_languages.values():
    print(lang)

print("\n")

for lang in set(favorite_languages.values()):
    print(lang)

print("\n")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'js'],
    'phil': ['python', 'php'],
    'evgeniy': ['c', 'c++'],
}

for name, langs in favorite_languages.items():
    print(name)
    for lang in langs:
        print(lang)

print("# --------------- #")

# message = input("Tell me something")
# print(message)

# name = input("Enter your name: ")
# print(f"Hello, {name}")
#
# age = input("How old are you?")
# age = int(age)
# if age >= 18:
#     print("Good!")
# elif age > 30:
#     print("Not good, you old")
# else:
#     print("Sorry")

print("# --------------- #")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\n Tell me something, and i'll repeat it..."
prompt += "\n Enter 'quit' to end program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

print("# --------------- #")
