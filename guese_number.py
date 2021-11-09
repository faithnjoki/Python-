import random

def  guess_num(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guese a number between 1 and {x}: '))
        if guess < random_number:
            print('sorry,guese again. Too low')
        elif guess > random_number:
            print('sory,guese too high')
        else: 
            print ('congrats, you guesed the correct number')



guess_num(5)
