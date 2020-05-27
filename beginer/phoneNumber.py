phoneNumber = input('Please enter your phone number in xxx-yyy-zzzz format: ')
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

converted: str = ''
for item in phoneNumber:
    if item != '-':
        converted += numbers.get(item) + ' '
    else:
        converted += item + ' '
print(converted)