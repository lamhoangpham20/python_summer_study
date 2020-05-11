usernames = ['admin', 'Jaden', 'Bon', 'Soobin', 'Touliver']
current_users = ['Kitty', 'Thinh', 'Huy', 'Max', 'Huan']
new_users = ['Huan' ,'Thinh', 'Hung', 'Tai', 'Max']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
if usernames:
    pass
else:
    print('We need to find some users!')
current_users_lowercase = []
for username in current_users:
    current_users_lowercase.append(username.lower)
for username in new_users:
    if username.lower in current_users_lowercase:
        print('Please create new username')
    else:
        print('This username is available')

