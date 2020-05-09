# task 4.1
pizzas = ['Pepperoni', 'Hawaii', 'Blue cheese']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really love pizza!")
# task 4.2
pets = ['cat', 'dog', 'parrot', 'chicken', 'hamster']
for pet in pets:
    print(f"A {pet} would make a great pet.")
print('Any of these animals would make a great pet!')
# task 4.10
print("The first three items on the list are:")
for pet in pets[:3]:
    print(pet)
print("The first three items on the list are:")
for pet in pets[1:4]:
    print(pet)
print("The first three items on the list are:")
for pet in pets[-3:]:
    print(pet)
# task 4.11
friend_pizzas = pizzas[:]
pizzas.append('salami')
friend_pizzas.append('seafood')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)    