#!/usr/bin/python3
"""python input output"""


class Student:
    """ class that defines a student """

    """ instantiation """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        """ method """

    def to_json(self, attrs=None):
        """
        public method that returns the dictionary dscription
        with simpe data structre
        """
        if attrs is None:
            return self.__dict__
        else:
            stds = {}
            for attribute in attrs:
                if hasattr(self, attribute):
                    """ hasattr function, to check if an attribute exist """
                    stds[attribute] = getattr(self, attribute)
                    """
                    getattr function returns the value of the
                    specified attribute from the specified object.
                    """
            return stds
