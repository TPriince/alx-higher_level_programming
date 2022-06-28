#!/usr/bin/python3
"""
0-add_integer module
Returns the addition of two integers

"""


def add_integer(a, b=98):
    """ Function that adds two integers a and b,
    and raises an error if a and b are not integers
    or floats
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return result
