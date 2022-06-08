#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_list = []
    a_list = []
    b_list = []
    c_list = []

    for i in matrix[0]:
        n_list.append(i ** 2)

    for i in matrix[1]:
        a_list.append(i ** 2)

    for i in matrix[2]:
        b_list.append(i ** 2)

    c_list = list((n_list, a_list, b_list))

    return c_list
