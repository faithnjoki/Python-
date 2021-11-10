name = input('Your name: ')
print(f' Hey {name}, Welcome to my computer quiz game!')

Playing = input(f'{name} Do you want to play my game? yes or no ')
if Playing != 'yes':
        quit()
else:
    print('Thank you for choosing to play my game, All the best........')
    score = 0

# question 1
answer = input('What date was Leon Born? ')
if answer == '8':
    print('correct!')
    score += 1
else:
    print('Incorrect!') 

# question 2
answer = input('What day was Leon Born? ')
if answer == 'Sunday':
    print('correct!')
    score += 1
else:
    print('Incorrect!')

# question 3
answer = input("What is Leon's Surname? ")
if answer == 'Ndemo':
    print('correct!')
    score += 1
else:
    print('Incorrect!')


# question 4
answer = input("What is Leon's Second name? ")
if answer == 'Ronald':
    print('correct!')
    score += 1
else:
    print('Incorrect!')


# question 5
answer = input('What time was Leon born? ')
if answer == '8:50':
    print('correct!')
    score += 1
else:
    print('Incorrect!')


# question 6
answer = input("What is Leon's second name? ")
if answer == 'Ronald':
    print('correct!')
    score += 1
else:
    print('Incorrect!')


# question 7
answer = input("What was   Leon's  Birth weight Surname? ")
if answer == '3':
    print('correct!')
    score += 1
else:
    print('Incorrect!')


# question 8
answer = input("Which year was Leon born? ")
if answer == '2019':
    print('correct!')
    score += 1
else:
    print('Incorrect!')


# question 9
answer = input("Which Was the first word Leon said? ")
if answer == 'papa':
    print('correct!')
    score += 1
else:
    print('Incorrect!')


# question 10
answer = input("Between mom and dad, who does Leon Resemble the most? ")
if answer == 'dad':
    print('correct!')
    score += 1
else:
    print('Incorrect!')



