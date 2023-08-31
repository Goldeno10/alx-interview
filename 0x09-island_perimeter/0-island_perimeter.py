#!/usr/bin/python3
"""
Interview Task:
    Create a function def island_perimeter(grid): that returns
    the perimeter of the island described in grid:

    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn't have “lakes” (water inside that isn't connected
    to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    Compute the perimeter of an island described in grid
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    count += 1
                if j == 0 or grid[i][j - 1] == 0:
                    count += 1
                if i == (len(grid) - 1) or grid[i + 1][j] == 0:
                    count += 1
                if j == (len(grid[0]) - 1) or grid[i][j + 1] == 0:
                    count += 1
    return count
