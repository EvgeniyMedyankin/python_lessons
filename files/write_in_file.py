filename = 'text_files/programming.txt'

"""Записать в файл"""

with open(filename, 'w') as file_object:
    file_object.write('I love Python!\n')
    file_object.write('I love JS!\n')

"""Дописать в файл"""

with open(filename, 'a') as file_object:
    file_object.write('I love ReactJS!\n')
    file_object.write('I love NodeJS!\n')

"""Чтение файла с обработкой исключений"""

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry {filename} not found")  # pass - пропустить не выводя ошибку
else:
    print(contents)
