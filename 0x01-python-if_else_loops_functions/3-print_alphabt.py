#!/usr/bin/python3
'''
program that prints the ASCII alphabet.
In lowercase, not followed by a new line.
Print all the letters except q and e.
'''

for alpha in range(97, 122):
    if alpha != 101 and alpha != 113:
        print('{}'.format(chr(alpha)), end='')
