#!/usr/bin/python3
""" same object """


def is_same_class(obj, a_class):
    """function return True if the object exactly
    an instance of the specified class ; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    return False
