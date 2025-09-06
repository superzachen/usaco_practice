#https://codeforces.com/contest/2009/problem/B
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
for test_case in range(int(input())):
    x, y, k = map(int, input().split())
    operations_x = (x + k - 1) // k
    operations_y = (y + k - 1) // k
    result = max(2 * operations_x - 1, 2 * operations_y)

    print(result)