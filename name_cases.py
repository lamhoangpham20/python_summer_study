#task 2.3
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)
#task 2.4
print(name.upper())
print(name.lower())
print(name.title())
#task 2.5
message = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(message)
#task 2.6
famous_name = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
message = f'{famous_name} once said, "{quote}"'
print(message)
#task2.7
famous_name = "\t Albert Einstein"
message = f'{famous_name} once said, "{quote}"'
print(message)
famous_name = "\n Albert Einstein"
message = f'{famous_name} once said, "{quote}"'
print(message)
famous_name = "\n \t Albert Einstein \t"
message = f'{famous_name} once said, "{quote}"'
print(message)
message = f'{famous_name.lstrip()} once said, "{quote}"'
print(message)
message = f'{famous_name.rstrip()} once said, "{quote}"'
print(message)
message = f'{famous_name.strip()} once said, "{quote}"'
print(message)