from random import choice
lottery = ['0', '1', '2', '3', '4', '5', '6',
           '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
winner_lottery = []
print('The lottery winner is: ')
for x in range(0, 4):
    winner_lottery.append(choice(lottery))
print(winner_lottery)
my_ticket = 'abc9'
trial_times = 0
win = False
while win == False:
    winning_ticket_characters = []
    for x in range(0, 4):
        winning_ticket_characters.append(choice(lottery))
    winning_ticket = ''
    for character in winning_ticket_characters:
        winning_ticket = winning_ticket + character
    if winning_ticket == my_ticket:
        win = True
    trial_times = trial_times + 1
    print(trial_times)
