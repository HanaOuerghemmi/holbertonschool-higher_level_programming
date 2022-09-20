#!/usr/bin/python3
"""class square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
          return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
              raise TypeError(
                  "position must be a tuple of 2 positive integers")
        else:
            self.__positon = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
