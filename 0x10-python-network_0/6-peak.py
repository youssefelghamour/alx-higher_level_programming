#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers """

    if not list_of_integers:
        return None

    li = list_of_integers

    m = len(li) // 2

    if (m-1 < 0 or li[m-1] < li[m]) and (m+1 >= len(li) or li[m] > li[m+1]):
        return li[m]

    if m + 1 < len(li) and li[m + 1] > li[m - 1]:
        return find_peak(li[m:])
    else:
        return find_peak(li[:m])
