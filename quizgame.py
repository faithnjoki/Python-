name = input('Your name: ')
print(f' Hey {name}, Welcome to my computer quiz game!')

Playing = input(f'{name} Do you want to play my game?')
if Playing != 'yes':
        quit()
else:
    print('Thank you for choosing to play my game, All the best')

answer = input('What date was Leon Born? ')
if answer == '8':
    print('correct!')
else:
    print('Incorrect!')   