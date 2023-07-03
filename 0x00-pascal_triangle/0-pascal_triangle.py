#!/usr/bin/python3
'''
Contains function def pascal_triangle(n) that returns a list of lists of
integers representing the Pascal’s triangle of n.
'''


def pascal_triangle(n):
    '''
    Computes the pascals triangle
    args:
        n(int): degree integer
    Returns a 2D lists of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    '''
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        triangle.append([1] * (i + 1))
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle
