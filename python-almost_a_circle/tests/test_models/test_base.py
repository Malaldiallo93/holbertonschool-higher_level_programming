#!/usr/bin/python3
"""Unittest for Base Class in base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_empty(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id(self):
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_nb_objects(self):
        Base.__nb_objects = 0


class TestStaticMethods(unittest.TestCase):

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        s = Square(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        json_string = []
        self.assertEqual("[]", Base.to_json_string(json_string))

    def test_to_json_string_none(self):
        json_string = None
        self.assertEqual("[]", Base.to_json_string(json_string))


class TestClassMethods(unittest.TestCase):

    def test_from_json_string_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_square(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))


if __name__ == "__main__":
    unittest.main()