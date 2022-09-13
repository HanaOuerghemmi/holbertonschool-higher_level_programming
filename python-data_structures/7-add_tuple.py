#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    Atuple = tuple_a + (0, 0)
    Btuple = tuple_b + (0, 0)
    a = Atuple[0] + Btuple[0]
    b = Atuple[1] + Btuple[1]
    tuble_c = (a, b)
    return tuble_c
