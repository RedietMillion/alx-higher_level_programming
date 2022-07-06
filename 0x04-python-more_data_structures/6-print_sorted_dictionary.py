#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Parameters
        ----------
        filename: dictionary
        Returns
        ----------
        None
        """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
