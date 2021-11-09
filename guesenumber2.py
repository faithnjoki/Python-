#Come up with a secret number and have the computer try to guese it 
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ' '
    while feedback !='c':
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} to high (H),too low (L) or correct (C)')
        if feedback =='h':
            high = guess -1
        elif feedback == 'l':
            low = guess+1
    print('yay, the computer guesed your number {guess} correctly')


computer_guess(10)


