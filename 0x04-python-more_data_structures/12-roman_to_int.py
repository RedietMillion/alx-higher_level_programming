#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Parameters
        ----------
        filename: string
        Returns
        ----------
        Integers
        """
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    p = 0

    if type(roman_string) is str and roman_string:
        for i in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[i]] >= p:
                res += val[roman_string[i]]
            else:
                res -= val[roman_string[i]]
            p = val[roman_string[i]]
    return res
