person = {
    'first_name': 'Lam',
    'last_name': 'Pham',
    'age': 20,
    'city': 'Oulu'
}
first_name = person.get('first_name', 'unknown')
print(first_name)
last_name = person.get('last_name', 'unknown')
print(last_name)
age = person.get('age', 'unknown')
print(age)
city = person.get('city', 'unknown')
print(city)

favourite_number = {
    'jane': 26,
    'jack': 12,
    'cris': 7,
    'peter': 2,
    'bill': 6
}
number = favourite_number['jane']
print(f"Jane's favorite number is {number}.")
number = favourite_number['jack']
print(f"Jack's favorite number is {number}.")
number = favourite_number['cris']
print(f"Cris's favorite number is {number}.")
number = favourite_number['peter']
print(f"Peter's favorite number is {number}.")
number = favourite_number['bill']
print(f"Bill's favorite number is {number}.")
# task 6.7
person1 = {
    'first_name': 'Thinh',
    'last_name': 'Nguyen',
    'age': 20,
    'city': 'Oulu'
}
person2 = {
    'first_name': 'Huy',
    'last_name': 'Lee',
    'age': 20,
    'city': 'Oulu'
}
people = [person, person1, person2]
for man in people:
    print(f"Hello {man.get('first_name')} {man.get('last_name')}, {man.get('age')} years old, lives in {man.get('city')}. ")
#task 6.10
favourite_number = {
    'jane': [26, 6],
    'jack': [12, 2],
    'cris': [7, 25],
    'peter': [2, 8],
    'bill': [6, 8]
}
for name, numbers in favourite_number.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(number)

#task 6.11
cities = {
    'London': {
        'country':'England',
        'population':'8m',
        'fact': 'sadfsdf'
    },
    'Paris': {
        'country':'France',
        'population':'7m',
        'fact': 'city of light'
    },
    'Oslo': {
        'country':'Norway',
        'population':'1m',
        'fact': 'expensive'
    }
}
for city, info in cities.items():
    print(f"{city} is in {info.get('country')}")
    print(f"Population: {info.get('population')}")
    print(f"fact: {info.get('fact')}")
