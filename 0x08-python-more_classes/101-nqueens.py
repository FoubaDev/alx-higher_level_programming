#!/usr/bin/python3

"""Solves the n-queens puzzle using iterative backtracking."""

import sys


def check_placement(board, row, col):
    """Checks if placing a queen at (row, col) is valid.

    Args:
        board: A list representing the placement of queens.
        row: The row to check for valid placement.
        col: The column to check for valid placement.

    Returns:
        True if the placement is valid, False otherwise.
    """

    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return False
    return True


def solve_n_queens(n):
    """Solves the n-queens problem using iterative backtracking.

    Args:
        n: The number of queens in the problem.

    Returns:
        A list of solutions, where each solution is a list of queen positions.
    """

    solutions = []
    stack = []
    row = 0
    col = 0

    while True:
        if check_placement(stack, row, col):
            stack.append(col)
            if row == n - 1:
                # Found a solution
                solutions.append(stack[:])
                stack.pop()
                col += 1
            else:
                row += 1
                col = 0
        else:
            col += 1

        while col >= n or (len(stack) >= row + 1 and col >= stack[row]):
            if not stack:
                return solutions
            col = stack.pop() + 1
            row -= 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens <n>", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("n must be an integer", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("n must be at least 4", file=sys.stderr)
        sys.exit(1)

    solutions = solve_n_queens(n)

    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])
