#!/usr/bin/python3
"""
class squaire
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class squaire tht inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

        """
        task 11 update square add setter
        and getter for the public size
        """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
