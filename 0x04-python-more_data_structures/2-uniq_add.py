#!/usr/bin/python3
import functools


def uniq_add(my_list=[]):
    new_list = set(my_list)
    return functools.reduce(lambda x, y: x+y, new_list)
