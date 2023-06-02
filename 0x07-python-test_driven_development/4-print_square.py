#!/usr/bin/python3
<<<<<<< HEAD
"""Module containing a function that prints a square"""


def print_square(size):
    """ adds integers
        Arguments:
            @size: size of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        return
=======
"""
This is the print_square module.
The print_square module provides a simple function print_square()
that prints a square with #.
"""


def print_square(size):
    """Print square with #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
>>>>>>> 48e0916cb9b981d85ea35d6b8b6193e4b548abd7
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
