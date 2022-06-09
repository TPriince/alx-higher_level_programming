#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    num_1 = 0
    num_2 = 0

    for i in my_list:
        num_1 = num_1 + (i[0] * i[1])
        num_2 = num_2 + i[1]

    weight_value = num_1 / num_2
    return weight_value
