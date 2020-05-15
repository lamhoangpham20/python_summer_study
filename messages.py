def show_messages(messages):
    """This function shows messages"""
    for message in messages:
        print(message)


def send_messages(messages, sent_message):
    while messages:
        new_message = messages.pop()
        sent_message.append(new_message)


sent_messages = []
messages = ["hello", "shut up", "please"]
show_messages(messages)
send_messages(messages[:], sent_messages)
show_messages(sent_messages)
