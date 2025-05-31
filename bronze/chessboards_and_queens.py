# https://cses.fi/problemset/task/1624
# -- Helpers --
import sys
import os

problem_name = "speeding"

input_file = f"{problem_name}.in"
output_file = f"{problem_name}.out"

if os.path.exists(input_file):
    sys.stdin = open(input_file, "r")
    sys.stdout = open(output_file, "w")


def read_int():
    """Reads a single integer from a line."""
    return int(sys.stdin.readline())


def read_str():
    """Reads a single string from a line."""
    return sys.stdin.readline().strip()


def read_ints():
    """Reads multiple integers from a line, separated by space."""
    return list(map(int, sys.stdin.readline().split()))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()


# -- End of Helpers --
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens(board, row, n, count, reserved_squares):
    if row == n:
        count[0] += 1
        return

    for col in range(n):
        if (row, col) not in reserved_squares and is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, count, reserved_squares)
n = 8
board = [0] * n
count = [0]
reserved_squares = set()

for r in range(n):
    row_input = input()
    for c in range(n):
        if row_input[c] == '*':
            reserved_squares.add((r, c))
    
solve_n_queens(board, 0, n, count, reserved_squares)
print(count[0])