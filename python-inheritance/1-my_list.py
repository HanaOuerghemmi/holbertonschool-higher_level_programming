#!/usr/bin/python3
""" My list """


class MyList(list):
    """ class Myliist """

    def print_sorted(self):
        """ public instance method that print sorted list """

        print(sorted(self))
