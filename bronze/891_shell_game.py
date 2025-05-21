# https://usaco.org/index.php?page=viewproblem2&cpid=891
# -- Helpers --
import sys
import os

problem_name = "shell"

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
shells = [1, 2, 3]
scores = [0, 0, 0]# For each different pos

for _ in range(n):
    a, b, g = read_ints()
    shells[a - 1], shells[b - 1] = shells[b - 1], shells[a - 1]
    scores[shells[g - 1] - 1] += 1

print(max(scores))