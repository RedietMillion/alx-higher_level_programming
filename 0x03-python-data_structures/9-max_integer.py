#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """Find the biggest integer of a list.
    Parameters
        ----------
        filename: my_list
        Returns
        ----------
        Integer
     """
    if len(my_list) == 0:
        return (None)
    Max = my_list[0]
    for j in range(len(my_list)):
        if my_list[j] > Max:
            Max = my_list[j]
    return (Max)
