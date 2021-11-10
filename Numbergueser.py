# import random module
import random


# random.randrange(start,stop)
# random.randrange(6,8), This generates random numbers between 6 and 8 but wont generate 8. Incase you wate to generate 8 you have to add 9 as the end point
# random.randrange(8) generates numbers between 0-8 and not 8

# random.randint(start,stop)
# random.randint(6,8), This generates random numbers between 6 and 8and  generates 8 too.


# number = random.randrange(7,12)
# print(number)

number = input('Type a number: ')
if number.isdigit():
    number = int(number)
    if number <= 0:
        print('please type a  number larger than 0 next time ')
        quit()
else:
    print("please type a number next time")
    quit()

random_number = random.radint(number)
print(random_number)