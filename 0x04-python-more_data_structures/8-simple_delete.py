#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
     Parameters
        ----------
        filename: dictionary
        Returns
        ----------
        dictionary
     """
    a_dictionary.pop(key, None)
    return a_dictionary
