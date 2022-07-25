#!/usr/bin/python3
'''
Module for an empty class for rectangle
'''


class Rectangle:
    '''
    Class  rectangle
    '''
    def __init__(self, width=0, height=0):
        '''
        Instantiation
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''
        Property width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        property setter value of width as an integer.
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Property height.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Property setter value of height as an integer.
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
