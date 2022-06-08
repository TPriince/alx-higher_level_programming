#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []

    for i in range(len(matrix)):
        y = list(map(lambda x: x**2, matrix[i]))
        new_list.append(y)

    return new_list
