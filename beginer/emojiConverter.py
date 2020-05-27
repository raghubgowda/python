def convert_message(message: str):
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    output = ''
    for item in message.split(' '):
        output += emojis.get(item, item) + ' '
    return output


msg = input(">: ")
print(convert_message(msg))
