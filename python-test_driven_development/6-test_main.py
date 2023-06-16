#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

# Multiples tests for Unittest - 6-max_integer
print(max_integer([1, 2, 3, 4]))
print(max_integer([-1, -3, -4, -2]))
print(max_integer([-1, 3, -4, 2]))
print(max_integer([1, 5.4, 4, -2]))
print(max_integer([2]))
print(max_integer([-5]))
print(max_integer())
print(max_integer([1, 1]))
print(max_integer(["str", 2, 3]))
print(max_integer([False, True, 3]))
print(max_integer([True, "str", 3]))
print(max_integer("higher ASCII value is : v"))
print(max_integer(False))
