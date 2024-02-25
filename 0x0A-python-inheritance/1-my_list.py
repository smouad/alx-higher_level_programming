#!/usr/bin/python3
"""
contains the MyList class
"""


class Mylist(list):
    """A class that inherits from list."""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
    