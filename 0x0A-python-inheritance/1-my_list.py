#!/usr/bin/python3
"""My list

Done By: Rediet M.
"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
