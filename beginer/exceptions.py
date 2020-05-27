try:
    yob = int(input('Enter a your year of birth: '))
    salary = int(input('Enter you salary: '))
    age = 2020 - yob
    retirement_benefits = (65 - age) * 20000 / salary
    print(f'You are {age} years old and you will get ${retirement_benefits} retire benefits')
except ZeroDivisionError:
    print('Salary cannot be 0')
except ValueError:
    print('Please enter year of birth in YYYY format')
finally:
    print('In finally!!!')
