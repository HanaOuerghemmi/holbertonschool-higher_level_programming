#!/usr/bin/python3
"""python input output"""

import json

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
        else :
            return json.dumps(attrs)
