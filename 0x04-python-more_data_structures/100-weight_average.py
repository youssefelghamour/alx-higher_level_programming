#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    avg = 0
    weight = 0
    for tup in my_list:
        weight += tup[1]
        avg += tup[0] * tup[1]

    return avg / weight
