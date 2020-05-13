favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
people = ['jen', 'cris', 'phil', 'ben']
for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, Thanks for responding")
    else:
        print(f"{name.title()}, Please register the poll")