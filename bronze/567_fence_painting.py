#https://usaco.org/index.php?page=viewproblem2&cpid=567
# -- Helpers --
import sys
import os

problem_name = "cow_evo"

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
a, b = read_ints()
c, d = read_ints()
overlapping = False
if a < d and c < b or c < b and a < d:
    overlapping = True
total_length = 0
if overlapping:
    total_length = abs(b - c)
else:
    total_length = b-a + d-c
print(total_length)
