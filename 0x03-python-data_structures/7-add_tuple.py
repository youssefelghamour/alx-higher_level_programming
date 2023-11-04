#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a > 0:
        a1 = tuple_a[0]
    else:
        a1 = 0
    if len_a > 1:
        a2 = tuple_a[1]
    else:
        a2 = 0

    if len_b > 0:
        b1 = tuple_b[0]
    else:
        b1 = 0
    if len_b > 1:
        b2 = tuple_b[1]
    else:
        b2 = 0

    return (a1 + b1, a2 + b2)
