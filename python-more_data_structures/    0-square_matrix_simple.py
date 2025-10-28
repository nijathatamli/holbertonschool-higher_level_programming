#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squeared_matrix = []
    for x in matrix:
        part_of_matrix = []
        for i in x:
            part_of_matrix.append(i**2)
        squeared_matrix.append(part_of_matrix)
    return squeared_matrix
