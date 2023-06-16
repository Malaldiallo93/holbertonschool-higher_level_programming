#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittest with :
    - Module that test correct input
    - Module that test empty list
    - Module that test types input
    """
    def test_area(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, -2, -4, -3]), -1)
        self.assertAlmostEqual(max_integer([-1, 3, -4, 2]), 3)
        self.assertAlmostEqual(max_integer([1, 5.4, 4, -2]), 5.4)
        self.assertAlmostEqual(max_integer([2]), 2)
        self.assertAlmostEqual(max_integer([-5]), -5)
        self.assertAlmostEqual(max_integer([1, 1]), 1)

    def test_empty(self):
        self.assertIsNone(max_integer(), None)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, ["str", 2, 3])
        self.assertRaises(TypeError, max_integer, [True, "str", 3])
        self.assertRaises(TypeError, max_integer, False)
        self.assertAlmostEqual(max_integer([False, True, 3]), 3)
        self.assertAlmostEqual(max_integer("higher ASCII value is : v"), "v")