#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print()
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print()