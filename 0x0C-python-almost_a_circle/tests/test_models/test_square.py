#!/usr/bin/python3
""" Unit tests for the `Square` class"""
import unittest
import json
import sys
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Unit tests for the `Square` class"""
    def setUp(self):
        """ Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """ Docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_is_instance(self):
        """ Is instance"""
        self.assertTrue(isinstance(Square(1, 1), Square))

    def test_is_subclass(self):
        """ Is subclass"""
        self.assertTrue(issubclass(type(Square(1, 1)), Base))

    def test_empty_init(self):
        """ Empty init"""
        self.assertRaises(TypeError, Square, ())
