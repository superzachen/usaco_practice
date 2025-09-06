#https://codeforces.com/contest/1950/problem/C
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
def solve():
    h_m = read_str()
    h, m = map(int, h_m.replace(':', ' ').split())
    am_pm = " AM" if h < 12 else " PM"
    h = h % 12 if h % 12 != 0 else 12
    print(f"{h:02}:{m:02}{am_pm}")

t = read_int()
for _ in range(t):
    solve()