#!/usr/bin/python3
""" geometry module """


class BaseGeometry():
    """ Base gemetry class """

    def area(self):
        """
        Public instance method that raises an Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method:  hat validates value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ intialize rectangle """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
