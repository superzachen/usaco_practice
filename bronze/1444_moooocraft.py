#https://usaco.org/index.php?page=viewproblem2&cpid=1444
# -- Helpers --
import sys
import os
import math

problem_name = "balancing"

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
# -- Helpers --
import sys
import os

problem_name = "balancing"

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
n, q = read_ints()
xy = [[n] * n for _ in range(n)]
xz = [[n] * n for _ in range(n)]
yz = [[n] * n for _ in range(n)]

ans = 0

for _ in range(q):
    x, y, z = read_ints()

    # Decrement counts in each slice
    xy[x][y] -= 1
    xz[x][z] -= 1
    yz[y][z] -= 1

    # Count newly completed slices
    if xy[x][y] == 0:
        ans += 1
    if xz[x][z] == 0:
        ans += 1
    if yz[y][z] == 0:
        ans += 1

    print(ans)