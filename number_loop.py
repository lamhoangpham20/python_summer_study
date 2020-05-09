# task 4.3
for value in range(0, 21):
    print(value)
# task 4.4
numbers = []
for value in range(0, 1000001):
    numbers.append(value)
for number in numbers:
    pass
    # print(number)
# task 4.5
print(sum(numbers))
# task 4.6
odd_numbers = list(range(1, 20, 2))
for odd_number in odd_numbers:
    print(odd_number)
# task 4.7
triple_numbers = [value*3 for value in range(1, 11)]
for triple_number in triple_numbers:
    print(triple_number)
# task 4.8
cube = []
for value in range(1, 11):
    cube.append(value**3)
for number in cube:
    print(number)
# task 4.9
cube = [value**3 for value in range(1, 11)]
for number in cube:
    print(number)
