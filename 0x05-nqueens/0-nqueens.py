#!/usr/bin/python3
"""N queens puzzle"""


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check for another queen in this column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, row, n, results):
    """Recursive function to find all solutions."""
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        results.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, results)
            board[row][col] = 0  # Backtrack


def nqueens(n):
    """Main function to solve the N Queens problem"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    results = []
    solve_nqueens(board, 0, n, results)
    for solution in results:
        print(solution)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
