def show_city(city, country, population=''):
    if population:
        string = f"{city.title()}, {country.title()} - population {population}"
        return string
    else:
        string = f"{city.title()}, {country.title()}"
        return string