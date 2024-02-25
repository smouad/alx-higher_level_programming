#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list."""
    def print_sorted(self):
        """Print a sorted list."""
        print(sorted(self))
