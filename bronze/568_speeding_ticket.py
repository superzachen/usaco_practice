# https://usaco.org/index.php?page=viewproblem2&cpid=568
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
n, m = read_ints()

speedlim = []
for _ in range(n):
    length, speed = read_ints()
    speedlim.extend([speed] * length)

bessielim = []
for _ in range(m):
    length, speed = read_ints()
    bessielim.extend([speed] * length)

max_speeding = 0
for i in range(100):
  max_speeding = max(max_speeding, bessielim[i] - speedlim[i])
print(max_speeding)