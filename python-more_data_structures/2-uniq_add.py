#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = []
    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return sum(unique_numbers)
