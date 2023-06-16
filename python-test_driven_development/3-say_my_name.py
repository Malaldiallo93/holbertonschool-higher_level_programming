#!/usr/bin/python3
"""Module prints My name is <first name> <last name>
    Args:
        first_name (string): string to write
        last_name (string): string to write
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    full_name = first_name + " " + last_name
    print("Mon nom est", full_name)
