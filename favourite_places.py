favourite_places = {
    'Huy': ['Viena', 'Hanoi', 'Seoul'],
    'Thinh': ['Rome', 'Paris', 'Budapest'],
    'Lam': ['Munich', 'Hoian', 'Danang']
}
for name, places in favourite_places.items():
    print(f"{name}'s favourite places are:")
    for place in places:
        print(place)
