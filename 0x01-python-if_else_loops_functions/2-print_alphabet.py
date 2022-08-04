#!/usr/bin/python3
'''
program that prints the ASCII alphabet, in lowercase.
'''


def lower_case():
    '''
    class for lower case
    '''
    for alpha in range(97, 123):
        print("{}".format(chr(alpha)), end='')


lower_case()
