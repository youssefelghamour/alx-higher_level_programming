#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        arg = sys.argv[1:]
        print("1 argument:")
        print("{}: {}".format(1, arg[0]))
    else:
        arg = sys.argv[1:]
        print("{} arguments:".format(length))
        for i in range(1, length+1):
            print("{}: {}".format(i, arg[i-1]))
