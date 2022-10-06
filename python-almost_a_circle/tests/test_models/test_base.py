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
