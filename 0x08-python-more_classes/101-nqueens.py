#!/usr/bin/python3
"""INSPIRED SOLUTION."""


import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board INSPIRED SOLUTION."""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_util(board, col, N, solutions):
    """Utilizes backtracking to find all solutions INSPIRED SOLUTION."""
    if col == N:
        solutions.append(board[:])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[col] = i
            solve_nqueens_util(board, col + 1, N, solutions)


def solve_nqueens(N):
    """Solve the N-Queens problem and print the solutions INSPIRED SOLUTION."""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
solve_nqueens(sys.argv[1])
