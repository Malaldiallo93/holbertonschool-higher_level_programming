#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
        print("{:c}".format(ascii_value), end="")
    print()
