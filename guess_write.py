enter = True
while enter:
    name = input("Please enter your name")
    if name == 'quit':
        enter = False
    else:
        print(f'\n {name}')
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f"\n{name}")