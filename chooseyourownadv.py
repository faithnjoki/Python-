name = input('What is your name? ')
print(f' Hey {name}, Welcome to this adventure!')

answer = input('You Have reached the end of your road, you can choose to turn left ot turn right. Which one do you choose ').lower()
if answer == 'left':
    answer = input('You come to a river,You can walk around it or swim across.Type walk to walk around and swim to swim across. ').lower()
    if answer == 'swim':
       print('You swim across and were eaten by an alligator.')
    elif  answer == 'walk':
       print('You walked for many miles and you became hungry and you lost the game.')
    else:
        print('Not a valid option. You Lose')

elif answer == 'right':
    answer = input('You come to a hill, Do you want to cross or go back.. Type cross or back ').lower()
    if answer == 'go back':
       print('You go back and loose')
    elif answer == 'cross':
        answer = input('You cross the bridge and meet a strange, Do you talk to them or snob them? yes or no ').lower()
        if answer == 'yes':
            print('You made a wrong choice coz they will kidnap you')
        elif answer  == 'no':
            # print('You made a wise decision,Proceed')
            answer = input('Why dont you great stranger? Fear or pride ').lower()
            if answer == 'fear':
                print('You can do everything through Christ who strengthens you, Be strong!')
                print('Game ended, Goodbye....')
            elif answer == 'pride':
                print('It always comes before a fall')
            else:
                print('Not a valid option. You Lose')
            
        else:
            print('Not a valid option. You Lose')

    else:
        print('Not a valid option. You Lose')

    

else:
    print('You made an invalid Choice,You loose!')
