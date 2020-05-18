try:
    with open('ebook.txt','r') as f:
        content = f.read()
except FileNotFoundError:
    pass
else:
    print(content.lower().count('the ')) 