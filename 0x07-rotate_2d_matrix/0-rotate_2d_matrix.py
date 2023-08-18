#!/usr/bin/python3
"""
Task:
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will
     not be empty.
"""


def rotate_2d_matrix(matrix):
    """Rotates a matrix 90 degrees clockwise"""
    if matrix:
        n = len(matrix)

        # Transpose the matrix (swap elements across the diagonal)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse the rows to complete the clockwise rotation
        for i in range(n):
            matrix[i].reverse()
