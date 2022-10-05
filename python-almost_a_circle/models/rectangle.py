#!/usr/bin/python3
""" rectangle """

from models.base import Base

class Rectangle(Base):
    """
    classe Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ intialize rectangle """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
