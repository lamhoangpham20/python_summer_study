from function import display_message


def print_items(*sandwich_items):
    for item in sandwich_items:
        print(item)


print_items('bread', 'cheese')
print_items('bread', 'tomato', 'ham')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Lam', 'Pham',
                             location='oulu',
                             phone_number='0417166879',
                             address='yliopistokatu 18')
print(user_profile)


def make_car(manufacturer, model, **info):
    "dictionary of car"
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

display_message()
