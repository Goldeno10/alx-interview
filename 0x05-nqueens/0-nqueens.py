#!/usr/bin/python3
"""
Task:
    The N queens puzzle is the challenge of placing N non-attacking
      queens on an N×N chessboard. Write a program that solves the
      N queens problem.
    Usage: nqueens N
    If the user called the program with the wrong number of arguments,
     print Usage: nqueens N, followed by a new line, and exit with
     the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line,
     and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a new line,
     and exit with the status 1
    The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position on the board.

    Args:
        board (list): The N x N chessboard represented as a 2D list.
        row (int): The row index where the queen is to be placed.
        col (int): The column index where the queen is to be placed.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens problem and return all the possible solutions.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Returns:
        list: A list of all the solutions. Each solution is represented
         as a list of (row, col) positions of the queens.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        """implement backtrckig of the queen"""
        if row == N:
            solutions.append([[r, c] for r in range(N)
                              for c in range(N) if board[r][c] == 1])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_nqueens(N)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
