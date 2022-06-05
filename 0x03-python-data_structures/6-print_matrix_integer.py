#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for list in matrix:
        for item in list:
            if item != list[-1]:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item), end="")
        print('')
