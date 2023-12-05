#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a)
    size2 = len(tuple_b)
    if size1 < 2:
        tuple_a += (0, 0)
    if size2 < 2:
        tuple_b += (0, 0)

    new_tuple = tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1]
    return new_tuple
