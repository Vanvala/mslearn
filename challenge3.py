import random

guess = random.randint(1, 10)
answer = 0
tries = 0

while guess != answer:
    tries += 1
    answer = input(f'Guess a number between 1 and 10 \n Enter guess #{tries}: ')

    if answer.isalpha():
        print('Numbers only, please!')
        continue
    
    answer = int(answer)
    if answer > guess:
        print('Your guess is too high, try again!')
    else:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {tries} tries!')
