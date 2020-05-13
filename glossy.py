words= {
    'var': 'variable',
    'char': 'character',
    'dict': 'dictionary',
    'li': 'list',
}
print(f"\nvar is {words.get('var')}")
print(f"\nchar is {words.get('char')}")
print(f"\ndict is {words.get('dict')}")
print(f"\nli is {words.get('li')}")
for word, meaning in words.items():
    print(f"\n{word} is {meaning}")