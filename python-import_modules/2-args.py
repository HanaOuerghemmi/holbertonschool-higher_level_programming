#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print("0 argument.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{}argument:".format(c))
