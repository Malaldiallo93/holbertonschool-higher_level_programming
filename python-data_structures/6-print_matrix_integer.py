#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in matrix:
            for element in range(len(line)):
                if element == len(line) - 1:
                    print("{:d}".format(line[element]), end="")
                else:
                    print("{:d} ".format(line[element]), end="")
            print()
