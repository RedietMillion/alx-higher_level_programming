#!/usr/bin/python3
def best_score(a_dictionary):
    """
     Parameters
        ----------
        filename: dictionary
        Returns
        ----------
        Integer
     """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
