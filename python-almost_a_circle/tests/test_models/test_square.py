#!/usr/bin/python3
"""Unittest for Rectangle Class in rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square(self):
        s0 = Square(5)
        self.assertTrue(type(s0.width) is int)

    def test_str_type_arg(self):
        with self.assertRaises(TypeError):
            Square("2")

    def test_negative_int_type_arg(self):
        with self.assertRaises(ValueError):
            Square(-10)


class TestSquareMethods(unittest.TestCase):

    def test_area(self):
        s1 = Square(3)
        self.assertEqual(Square.area(s1), 9)

    def test_str(self):
        s2 = Square(5)
        self.assertEqual(Square.__str__(s2), "[Square] (17) 0/0 - 5")

    def test_update_one_arg(self):
        s3 = Square(5)
        s3.update(10)
        self.assertEqual("[Square] (10) 0/0 - 5", str(s3))

    def test_update_multiple_args(self):
        s4 = Square(5)
        s4.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s4))

    def test_update_one_kwarg(self):
        s5 = Square(5)
        s5.update(**{"size": 12})
        self.assertEqual("[Square] (22) 0/0 - 12", str(s5))

    def test_update_multiple_kwargs(self):
        s6 = Square(5)
        s6.update(**{'size': 7, 'id': 48, 'y': 1})
        self.assertEqual("[Square] (48) 0/1 - 7", str(s6))

    def test_to_dictionary(self):
        s7 = Square(10, 2, 1)
        output = {'id': 18, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(output, s7.to_dictionary())


if __name__ == "__main__":
    unittest.main()