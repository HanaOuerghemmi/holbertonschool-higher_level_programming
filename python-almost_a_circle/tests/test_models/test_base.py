#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import json
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """check functionality of Base class"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

class TestBase_to_json_string(unittest.TestCase):
    """ check it """

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

