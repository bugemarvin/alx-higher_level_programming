#!/usr/bin/python3
'''
function that prints the numbers from 1 to 100 separated by a space.
'''


def fizzbuzz():
    number = 1
    while number < 100:
        if number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 15 == 0:
            print('FizzBuzz')
        else:
            print('{}'.format(number))

        number += 1


fizzbuzz()
