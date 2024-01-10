#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret_matrix = []
    for i, rows in enumerate(matrix):
        ret_row = []
        for j, col in enumerate(rows):
            ret_row.append(col ** 2)
        ret_matrix.append(ret_row)
    return ret_matrix
