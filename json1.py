import json

numbers = [2, 5, 7, 9, 11, 13, 15]

filename = 'files/text_files/numbers.json'


def read_file(file_link):
    with open(file_link, encoding='utf-8') as f:
        print(json.load(f))


def show_file():
    try:
        read_file(filename)
    except FileNotFoundError:
        print("Data is dumped")
        with open(filename, 'w') as f:
            json.dump(numbers, f)
    else:
        return read_file(filename)


show_file()
