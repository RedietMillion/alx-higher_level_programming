#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """ It retrive an element from a list.
        Parameters
        ----------
        filename: my_list, index
        Returns
        ----------
        List
        Contain a list of elements
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
