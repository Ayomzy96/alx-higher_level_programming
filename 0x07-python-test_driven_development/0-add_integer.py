#!/usr/bin/python3
<<<<<<< HEAD
"""Module containing a dummy adder function for testing"""


def add_integer(a, b=98):
    """ adds integers
        Arguments:
        @a: first integer
        @b: second integer, defaults to 98 if not given
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
=======
'''
add_integer module
'''


def add_integer(a, b):
    """
    Return sum of a and b.
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return ( a + b )
>>>>>>> 48e0916cb9b981d85ea35d6b8b6193e4b548abd7
