secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    i = int(input('Make a guess: '))
    if i == secret_number:
        print('Awesome... You win!!!')
        break
    else:
        guess_count += 1
else:
    print('Sorry!!! You lost. Better luck next time!!!')
