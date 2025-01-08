#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)] 

    for row in range(n):
        for column in range(len(matrix[0])):
            result[column][n  -1 -row] = matrix[row][column]
    
    for  row in result:
        print(row)
