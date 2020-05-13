rivers = {
    'nile': 'egypt',
    'amazon': 'brazil'
}
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)