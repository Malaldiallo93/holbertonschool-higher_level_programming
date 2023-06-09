#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for element in my_list[:x]:
            print(element, end=" ")
        print()
        return min(x, len(my_list))
    except:
        return 0
