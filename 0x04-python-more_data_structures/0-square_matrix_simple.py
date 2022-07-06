#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Replace an element of a list at a specific position.
     Parameters
     ----------
     filename: matrix
     Returns
        ----------
        Lists
     """
    return [[x ** 2 for x in y] for y in matrix]
