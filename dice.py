from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))

dice = Dice()
print('Role 10 time 6-sided')
for x in range(0,10):
    dice.roll_dice()
dice2 = Dice(10)
print('Role 10 time 10-sided')
for x in range(0,10):
    dice2.roll_dice()
dice3 = Dice(20)
print('Role 10 time 20-sided')
for x in range(0,10):
    dice3.roll_dice()

