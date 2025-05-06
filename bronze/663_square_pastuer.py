# https://usaco.org/index.php?page=viewproblem2&cpid=663
# -- Helpers --
import sys
import os

problem_name = "blocks"

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
x1, y1, x2, y2 = read_ints()
x3, y3, x4, y4 = read_ints()

min_x = min(x1, x2, x3, x4)
max_x = max(x1, x2, x3, x4)
min_y = min(y1, y2, y3, y4)
max_y = max(y1, y2, y3, y4)

side = max(max_x - min_x, max_y - min_y)
print(side * side)
