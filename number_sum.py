mistake = True
while mistake:
    number1 = input('enter the first number')
    number2 = input('enter the second number')
    if (number1 == 'quit') or (number2 == 'quit'):
        mistake = False
    try:
        sum = int(number1) + int(number2)
    except ValueError:
        pass
    else:
        print(sum)
