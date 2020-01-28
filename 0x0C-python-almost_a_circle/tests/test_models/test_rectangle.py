#!/usr/bin/python3
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle

"""
Unittest cases for Rectangle class
"""


class RectangleTest(unittest.TestCase):

    def test_id(self):
        # Test to check the id

        Base._Base__nb_objects = 0

        r1 = Rectangle(3, 6)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 4)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_widthProperty(self):
        # Test the property of width

        r1 = Rectangle(2, 4)
        self.assertEqual(r1.width, 2)

    def test_heightProperty(self):
        # Test the property of height

        r1 = Rectangle(2, 4)
        self.assertEqual(r1.height, 4)

    def test_xProperty(self):
        # Test the property of x

        r = Rectangle(2, 7, 3, 9)
        self.assertEqual(r.x, 3)

    def test_yProperty(self):
        # Test the property of y

        r = Rectangle(8, 4, 3, 2)
        self.assertEqual(r.y, 2)

    def test_heightSetter(self):
        # Test if height is not a integer

        self.assertRaises(TypeError, Rectangle, 4, "luna")

    def test_heightNegative(self):
        # Test if the height is a negative number

        self.assertRaises(ValueError, Rectangle, 3, -9)

    def test_widthSetter(self):
        # Test if width is not a integer

        self.assertRaises(TypeError, Rectangle, "luna", 10)

    def test_widthNegative(self):
        # Test if the weight is a negative number

        self.assertRaises(ValueError, Rectangle, -4, 8)

    def test_xSetter(self):
        # Test if x is not a integer

        self.assertRaises(TypeError, Rectangle, 7, 10, "luna", 2)

    def test_xNegative(self):
        # Test if the x is a negative number

        self.assertRaises(ValueError, Rectangle, 9, 6, -4, 2)

    def test_ySetter(self):
        # Test if y is not a integer

        self.assertRaises(TypeError, Rectangle, 8, 10, 2, "luna")

    def test_yNegative(self):
        # Test if the y is a negative number

        self.assertRaises(ValueError, Rectangle, 10, 8, 4, -2)

    def testArea(self):
        # Test the method area:

        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(4, 6, 2, 0)
        self.assertEqual(r2.area(), 24)
        r3 = Rectangle(7900, 8903)
        self.assertEqual(r3.area(), 7900 * 8903)

    def test_areaError(self):
        # Test the area when there are not arguments

        self.assertRaises(TypeError, Rectangle)

    def test_documentation(self):
        # Test to verify if the documentation is created

        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)
