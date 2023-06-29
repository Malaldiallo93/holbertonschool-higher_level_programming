#!/usr/bin/python3
"""Unittest for Rectangle Class in rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        r0 = Rectangle(10, 2)
        self.assertTrue(type(r0.width) is int)

    def test_str_type_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_negative_int_type_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)


class TestRectangleMethods(unittest.TestCase):

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(Rectangle.area(r1), 6)

    def test_area_multiple(self):
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(Rectangle.area(r2), 56)

    def test_str(self):
        r3 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(Rectangle.__str__(r3), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_one_arg(self):
        r4 = Rectangle(10, 10, 10, 10)
        r4.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r4))

    def test_update_multiple_args(self):
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r5))

    def test_update_one_kwarg(self):
        r6 = Rectangle(10, 10, 10, 10)
        r6.update(**{"width": 2})
        self.assertEqual("[Rectangle] (12) 10/10 - 2/10", str(r6))

    def test_update_multiple_kwargs(self):
        r7 = Rectangle(10, 10, 10, 10)
        r7.update(**{'width': 2, 'x': 16, 'height': 24, 'id': 48})
        self.assertEqual("[Rectangle] (48) 16/10 - 2/24", str(r7))

    def test_to_dictionary(self):
        r8 = Rectangle(10, 2, 1, 9)
        output = {'height': 2, 'id': 8, 'width': 10, 'x': 1, 'y': 9}
        self.assertDictEqual(output, r8.to_dictionary())


if __name__ == "__main__":
    unittest.main()