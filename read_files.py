with open('learning_python.txt') as file_object:
    lines = file_object.read()
print(lines)
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
with open('learning_python.txt') as file_object:
    lines = file_object.read()
print(lines.replace('Python','C'))