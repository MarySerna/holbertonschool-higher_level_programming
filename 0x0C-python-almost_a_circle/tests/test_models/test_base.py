#!/usr/bin/python3
"""Unittest for Base module
"""


import unittest
import json
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Class for unittests
    """

    def test_id(self):
        """Test id
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(33)
        self.assertEqual(b3.id, 33)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_instance(self):
        """Test instance
        """
        base1 = Base()
        self.assertIsInstance(base1, object)

    def test_docstring(self):
        """Test docstring
        """
        self.assertIsNotNone(Base.__doc__)

    def test_pep8(self):
        """Test pep8
        """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/base.py"])
        self.assertEqual(pep.total_errors, 0)

    def test_to_json_string(self):
        """Test to json string
        """
        r = Rectangle(1, 3, 4, 5, 7)
        dic = r.to_dictionary()
        json_dic = r.to_json_string(dic)
        self.assertEqual(json_dic, json.dumps(dic))

    def test_json_string_to_file(self):
        """Test json string to file
        """
        r1 = Rectangle(2, 4, 6, 7, 3)
        r2 = Rectangle(5, 4, 5, 6, 9)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as file:
            new = file.read()
            t2 = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(new, json.dumps(t2))
