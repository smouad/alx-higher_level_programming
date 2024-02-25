#!/usr/bin/python3

class Mylist(list):
    """A class that inherits from list."""
    def print_sorted(self):
        print(sorted(self))
    