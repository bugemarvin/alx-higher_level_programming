#!/usr/bin/python3
'''function to create my list class
'''


class MyList(list):
    '''creating a class called my list.

    Attributes
    ----------

    list: self,
            This a inherited list from MyList
    '''

    def print_sorted(self):
        print(sorted(self, reverse=False))
        return self
