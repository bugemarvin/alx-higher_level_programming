#!/usr/bin/python3
'''
Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id#!/usr/bin/python3
'''


class Base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        
        def pub_instance(f_id, *id):
            if id is not None: 
                self.__nb_objects = f_id
            for a in id:
                __nb_objects += id
