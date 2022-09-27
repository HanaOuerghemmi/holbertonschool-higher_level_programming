#!/usr/bin/python3
""" geometry module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
     class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, size):
        """ intialize square """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
