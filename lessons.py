# print("# --------------- #")
#
# a = "Text string"
# print(a)
# print(a.upper())
# print(a.lower())
# a = a.lower()
# print(a.islower())
#
# print("# --------------- #")
#
# first_name = "evgeniy"
# last_name = "mediankin"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# message = f"Hello, {full_name.title()}"
# print(message)
# summa = 2 + 3
# print(summa)
# universe_age = 14_000_000_000
# print(universe_age)
# x, y, z = 0, 0, 0
# print(x, y, z)
# MAX_CONNECTIONS = 1000
# print(MAX_CONNECTIONS)
# MAX_CONNECTIONS = 3000
# print(MAX_CONNECTIONS)
#
# print("# --------------- #")
#
# auto = ["trek", "redline", "specialize"]
# print(auto[0])
# print(auto[-1])
# auto.append("skoda")
# print(auto)
# auto.insert(1, "honda")
# print(auto)
# del auto[0]
# print(auto)
#
# print("# --------------- #")
#
# motorcycles = ["honda", "ducati", "bmw", "yamaha"]
# print(motorcycles)
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
#
# print("# --------------- #")
#
# print(motorcycles)
# to_expensive = "ducati"
# motorcycles.remove(to_expensive)
# print(motorcycles)
# cars = ["bmw", "audi", "toyota", "subaru"]
# print(cars)
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars))
# print(len(cars))
# print(len(cars[0]))
#
# print("# --------------- #")
#
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(magician)
#
# for value in range(1, 10):
#     print(value)
#
# print("# --------------- #")
#
# numbers = list(range(1, 10))
# print(numbers)
#
# numbers = list(range(1, 10, 2))
# print(numbers)
#
# print("# --------------- #")
#
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
#
# print(squares)
#
# print("# --------------- #")
#
# digits = range(1, 10)
# print(min(digits))
# print(max(digits))
# print(sum(digits))
#
# print("# --------------- #")
#
# players = ["charles", "anna", " martina", "nikolai", "eli"]
# print(players)
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])
# print(players[:3])
# print(players[:])
#
# print("# ------Кортежи--------- #")
#
# dimensions = [200, 50]
# print(dimensions[0])
# print(dimensions[1])
# dimensions[0] = 250
# print(dimensions[0])
#
# print("# --------------- #")
#
# age = 55
# if age <= 25 or age == 30:
#     print("good!")
#
# request_toppings = ["mushrooms", "onions", "pineapple"]
#
# print('mushrooms' in request_toppings)
#
# age = 22
#
# if age == 18:
#     print("Age 18")
# elif age == 17:
#     print("Age 17")
# else:
#     print("Age default")
#
# rr = "ss2233"
# print(rr)
#
# print("# --------------- #")
#
# alien_0 = {'color': 'green', 'points': '5'}
# print(alien_0)
# print(f"Alien color is {alien_0['color']}")
# alien_0['color'] = 'red'
# print(f"Alien color is {alien_0['color']}")
# del alien_0['points']
# print(alien_0)
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value')
# print(point_value)
#
# for key, value in alien_0.items():
#     print(f"\n Key: {key}")
#     print(f" Value: {value}")
#
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     'evgeniy': 'js',
# }
#
# print("\n")
#
# for lang in favorite_languages.values():
#     print(lang)
#
# print("\n")
#
# for lang in set(favorite_languages.values()):
#     print(lang)
#
# print("\n")
#
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'js'],
#     'phil': ['python', 'php'],
#     'evgeniy': ['c', 'c++'],
# }
#
# for name, langs in favorite_languages.items():
#     print(name)
#     for lang in langs:
#         print(lang)
#
# print("# --------------- #")
#
# # message = input("Tell me something")
# # print(message)
#
# # name = input("Enter your name: ")
# # print(f"Hello, {name}")
# #
# # age = input("How old are you?")
# # age = int(age)
# # if age >= 18:
# #     print("Good!")
# # elif age > 30:
# #     print("Not good, you old")
# # else:
# #     print("Sorry")
#
# print("# --------------- #")
#
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# # prompt = "\n Tell me something, and i'll repeat it..."
# # prompt += "\n Enter 'quit' to end program. "
# # message = ""
# # while message != 'quit':
# #     message = input(prompt)
# #     print(message)
#
# # prompt = "\n Please enter name of city..."
# # prompt += "\n Enter 'quit' to end program. "
# # message = ""
# # while True:
# #     city = input(prompt)
# #     if city == 'quit':
# #         break
# #     else:
# #         print(f"I'd love to go to {city.title()}")
#
# print("# --------------- #")
#
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
#
# print("# --------------- #")
#
# unconfirmed_users = ['alice', 'jen', 'anna', 'tom']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verify user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print(f"\n The following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
#
# print("# --------------- #")
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'mouse', 'cat']
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)
#
# print("# --------------- #")

# responses = {}
# polling_active = True
#
# while polling_active:
#     name = input("What is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/no)")
#     if repeat == 'no':
#         polling_active = False
#
# print("\n --- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}")

# print("# --------------- #")
#
#
# def greet_user():
#     print('Hello World!')
#
#
# greet_user()
#
#
# def greet_user(username='Jessy'):
#     print(f"Hello, {username.title()}")
#
#
# greet_user()
# greet_user('tom')
#
#
# def get_formatted_name(first_name, last_name=''):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# to_format = get_formatted_name('Tom', 'Thomson')
# print(to_format)
#
# to_format = get_formatted_name('Tom')
# print(to_format)
#
#
# def make_pizza(*toppings):
#     print(toppings)
#     for topping in toppings:
#         print(topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'pepper', 'cheese')
#
# print("# --------------- #")
#
#
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile("evgeniy", "mediankin", location='Ukraine', age=31)
# print(user_profile)

print("# --------------- #")

"""
Заполнитель %s используется для представления строки (в данном случае 'Apple'), а заполнитель %d — для 
пред-ставления целого числа (1299). Если нужно добавить пробелы перед целым числом, то можно вставить число между % и 
d, чтобы указать желаемую длину строки. На-пример, "%5d" %(123) даст в результате " 123" (с двумя пробелами спереди и 
длиной 5).Заполнитель %f используется для форматирования чисел с плавающей точкой (чисел с десятичными точками). 
Здесь мы форматируем его как %4.2f, где 4 обозначает общую длину, а 2 обозначает 2 десятичных знака. Если нужно 
добавить пробелы перед числом, можно отформа-тировать его как %7.2f, что даст "   1.24" (с 2 десятич-ными знаками, 
3 пробелами спереди и длиной 7). 
"""

brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD' \
          'and the exchange rate is %4.2f USD to 1 EUR' \
          % (brand, 1299, exchangeRate)
print(message)

print("# --------------- #")
