pet1 = {
    'animal': 'cat',
    'owner': 'Louis'
}
pet2 = {
    'animal': 'dog',
    'owner': 'Max'
}
pet3 = {
    'animal': 'fish',
    'owner': 'Nimo'
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"{pet.get('owner')} has a {pet.get('animal')}")
