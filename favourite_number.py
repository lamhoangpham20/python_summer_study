import json


def show_number():
    try:
        with open('numbers.json', 'r') as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def enter_number():
    try:
        favourite_number = input('What is your favourite number? ')
        with open('numbers.json', 'w') as f:
            json.dump(favourite_number, f)
    except FileNotFoundError:
        pass

number = show_number()
if number:
    print(f'I know your favorite number! It’s {number}.')
else:
    enter_number()