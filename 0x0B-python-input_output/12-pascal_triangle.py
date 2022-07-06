#!/usr/bin/python3
"""
12-pascal_triangle module
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    a_list = [[0 for x in range(i + 1)] for i in range(n)]
    a_list[0] = [1]

    for i in range(1, n):
        a_list[i][0] = 1
        for j in range(1, i + 1):
            if j < len(a_list[i - 1]):
                a_list[i][j] = a_list[i - 1][j - 1] + a_list[i - 1][j]
            else:
                a_list[i][j] = a_list[i - 1][0]
    return a_list
