#!/usr/bin/python3
'''
program will assign a random signed number
to the variable number each time it is executed
'''

import random
number = random.randint(-10000, 10000)

'''
finding the last digit.
'''


l_digit = number % 10 if number >= 0 else ((-number % 10) * -1)


if l_digit > 5:
    print(f'Last digit of {number} is {l_digit} and is greater than 5')
elif l_digit == 0:
    print(f'Last digit of {number} is {l_digit} and is 0')
else:
    print(f'Last digit of {number} is {l_digit} and is less than 6 and not 0')
