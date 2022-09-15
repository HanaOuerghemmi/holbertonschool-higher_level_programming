#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        idx = 0
        for x in range(x):
            print('{:d}'.format(my_list[x]), end="")
            idx += 1
    except IndexError:
        pass
    finally:
        print()
        return idx

