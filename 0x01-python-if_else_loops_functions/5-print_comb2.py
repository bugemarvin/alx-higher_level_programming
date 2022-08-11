#!/usr/bin/python3
'''
program that prints numbers from 0 to 99.
'''


def numbers():
    for number in range(100):
        if number < 99:
            print('{}{}'.format(int(number / 10), number % 10), end=', ')
        else:
            print('{}{}'.format(int(number / 10), number % 10))


numbers()
