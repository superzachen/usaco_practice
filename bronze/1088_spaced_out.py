#https://usaco.org/index.php?page=viewproblem2&cpid=1088
# -- Helpers --
import sys
import os

problem_name = "tamingtheherd"

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
n = read_int()
grid_by_rows = [list(map(int, input().split())) for _ in range(n)]
grid_by_cols = zip(*grid_by_rows)

rows_alternate = 0
cols_alternate = 0

for i in range(n):
    #cow, no cow
    row = grid_by_rows[i]  # the ith row
    rows_alternate += max(sum(row[::2]), sum(row[1::2]))
    
    col = next(grid_by_cols)
    cols_alternate += max(sum(col[::2]), sum(col[1::2]))

print(max(rows_alternate, cols_alternate))