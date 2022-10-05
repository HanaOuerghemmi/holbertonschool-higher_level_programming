#!/usr/bin/python3
"""
base class
"""


class Base:
    """
    base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        function that create an object from json file
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
