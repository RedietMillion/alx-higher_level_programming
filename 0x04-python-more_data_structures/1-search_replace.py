#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Parameters
    ----------
    filename: my_list, search, replace
    Returns
    ----------
    Lists
    """
    return [replace if num == search else num for num in my_list]
