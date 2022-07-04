#!/usr/bin/python3
# 5-no_c.py
def no_c(my_string):
    """Remove all characters c and C from a string.
     Parameters
        ----------
        filename: my_string
        Returns
        ----------
        Strings
           Return string after replacing c and C
     """
    copy = [j for j in my_string if j != 'c' and j != 'C']
    return ("".join(copy))
