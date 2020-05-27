name = input('Enter the name')
len = len(name)
print(len)
if len < 3 :
    print('Name must be more than 3 characters')
elif len > 50:
    print('Name must be less than 50 characters')
else:
    print(f'Have a nice day {name}')
