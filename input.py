car = input("What kind of rental car you would like? ")
print(f"Let me see if I can find you a {car}.")
people = input("How many people are in your table group? ")
number = int(people)
if number > 8:
    print("You will have to wait")
else:
    print("Table is ready")
random_number = input("please enter a random number: ")
number = int(random_number)
if number % 10:
    print("Your number is multiple of 10")
else:
    print("Your number is not multiple of 10")