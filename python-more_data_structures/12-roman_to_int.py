#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    numerals = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    result = 0
    previous_value = 0

    for char in roman_string[::-1]:
        value = numerals.get(char, 0)
        if value >= previous_value:
            result += value
        else:
            result -= value
        previous_value = value

    return result
