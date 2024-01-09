#!/usr/bin/python3

"""
Write a class mylist thta inherits from list
"""


class Mylist(list):
    """
    Inherits from list
    Methods: print_sorted(self)
    """
    def __init__(self):
        """initializer for MyList"""
        super().__init__()

    def print_sorted(self):
        """prints the list(sorted) in ascending order
        type(int)
        """
        print(sorted(self))
