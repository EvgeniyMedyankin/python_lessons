"""Files-Reader"""

file_path = 'text_files/pi_digits.txt'

"""Считывание и полный вывод содержимого файла"""

with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())

print('\n#-----------#\n')

"""Считывание строчка за строчкой"""

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n#-----------#\n')

million_pi = 'text_files/one-million.txt'

with open(million_pi) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter you birthday in mmddyy:")
if birthday in pi_string:
    print("Yes, it's in pi")
else:
    print("Sorry :(")
print(f"\n{pi_string[:52]}\n")
print(len(pi_string))

print('\n#-----------#\n')
