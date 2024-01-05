#!/usr/bin/python3

"""Solve n-queens puzzle"""

import sys


def check_placement(board, row, col):
    """Ensure the position of the queen at (row, col).

    Args:
        board (list): Placement of queens.
        row (int): Row to check for valid placement.
        col (int): Column to check for valid placement.

    Returns:
        bool: True if the placement is valid, False otherwise.
    """
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return False
    return True


def solve_n_queens(n):
    """Uses iterative backtracking to solve the n-queens problem.

    Args:
        n (int): number of queens in the problem.

    Returns:
        list: A list of solutions.
    """
    solutions = []
    stack = []
    row = 0
    col = 0

    while True:
        if check_placement(stack, row, col):
            stack.append(col)
            if row == n - 1:
                solutions.append(stack[:])  # Found a solution
                stack.pop()
                col += 1
            else:
                row += 1
                col = 0
        else:
            col += 1

        while col >= n or (len(stack) >= row + 1 and col >= stack[row]):
            if len(stack) == 0:
                return solutions
            col = stack.pop() + 1
            row -= 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens n", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("n must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("n must be at least 4", file=sys.stderr)
        sys.exit(1)

    solutions = solve_n_queens(n)

    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])
