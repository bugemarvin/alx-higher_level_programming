#!/usr/bin/python3
'''
program that prints numbers from 0 to 99.
Numbers must be separated by ,, followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 2 print functions with string format
You can only use one loop in your code
'''


for number in range(100):
    if number < 99:
        print('{}{}'.format(int(number / 10), number % 10), end=', ')
    else:
        print('{}{}'.format(int(number / 10), number % 10))
