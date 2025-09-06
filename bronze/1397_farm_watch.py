#https://usaco.org/index.php?page=viewproblem2&cpid=1397
# -- Helpers --
import sys
import os
import math

problem_name = "It's mooin Time III"

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
n, q =  read_ints()
c = read_ints()
t = read_ints()
diffs = sorted([ci - ti for ci, ti in zip(c, t)], reverse=True)
for _ in range(q):
    V, S = read_ints()
    print("YES" if (V <= n and (V <= 0 or diffs[V-1] > S)) else "NO")