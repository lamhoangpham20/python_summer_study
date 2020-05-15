prompt = "Please add topping to your pizza \n"
stop = False
while stop == False:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f"You have ordered {toppings}")
prompt1 = "Please enter your age \n"
while stop == False:
    age = input(prompt1)
    if age == 'quit':
        break
    elif int(age) < 3:
        print('Your ticket is free')
    elif int(age) < 12:
        print('Your ticket is $10')
    elif int(age) > 12:
        print('Your ticket is $15')
