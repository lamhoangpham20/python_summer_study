from classes import Restaurant

restaurant = Restaurant('Itsudemo', 'Japanese')
print(f"{restaurant.restaurant_name} has {restaurant.cuisine_type} cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served(2)
print(restaurant.number_served)