files = ['cats.txt', 'dogs.txt']
for f in files:
    try:
        with open(f ,'r') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
