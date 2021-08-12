#second project=guess number from(User)-provider by (computer)

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    print("Guess a number between 1 and ",x)
    while guess != random_number:
        guess = int(input('Enter the number: '))
        if guess < random_number:
            print('Too low. Guess high')
        elif guess > random_number:
            print('Too high,Guess low')

    print('Correct ans')
guess(4)
