#https://codeforces.com/contest/1873/problem/A
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
t = read_int()
for _ in range(t):
    x = read_str()
    y = "abc"
    mistakes = 0
    for i in range(3):
        if x[i] != y[i]:
            mistakes += 1
    if mistakes == 3:
        print("NO")
    else:
        print('YES')