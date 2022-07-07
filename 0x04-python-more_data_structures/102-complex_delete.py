#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Parameters
        ----------
        filename: dictionary and its value
        Returns
        ----------
        Dictionary
    """
    for k, v in list(a_dictionary.items()):
        if v is value:
            a_dictionary.pop(k)
    return a_dictionary
