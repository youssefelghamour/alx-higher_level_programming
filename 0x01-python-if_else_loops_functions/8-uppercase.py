#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            m = 32
        else:
            m = 0
        print("{:c}".format(ord(c) - m), end='')
    print()
