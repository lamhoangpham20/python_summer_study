def display_message():
    """Display a message."""
    print("I am studying function")


display_message()


def favorite_book(title):
    """print the favourite book"""
    print(f"One of my favourite books is {title}")


favorite_book('Alice in the Wonderland')


def make_shirt(size="large", text_message="I love Python"):
    """print the favourite book"""
    print(
        f"The size of the shirt is {size}. The shirt has message: '{text_message}'")


make_shirt()
make_shirt(size='medium')
make_shirt(15, 'Hello')
make_shirt(size=15, text_message="Hello 2")


def describe_city(city, country='Finland'):
    print(f"{city.title()} is in {country.title()} ")


describe_city('Helsinki', 'Finland')
describe_city('Helsinki')
describe_city('Oslo', 'Norway')
