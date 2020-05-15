sandwich_orders = ['tuna', 'pastrami', 'meat',
                   'vegie', 'pastrami', 'tuna', 'pastrami']
print("We run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print(sandwich)
prompt = ("If you could visit one place in the world, where would you go?")
responses = {}
active = True
while active:
    name = input("what's your name")
    place = input(prompt)
    responses[name] = place
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
for name, place in responses.items():
       print(f"{name} would like to go to {place}.")
        