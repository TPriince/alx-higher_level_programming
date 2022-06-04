#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    z = tuple((x, y))
    return z
