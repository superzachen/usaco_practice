#https://codeforces.com/contest/2094/problem/B
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
def solve():
    n, m, l, r = read_ints()
    diff = n - m
    l = abs(l)
    if l >= diff:
        l -= diff
        diff = 0
    else:
        diff -= l
        l = 0
    print(-l, r - diff)


t = read_int()
for i in range(1, t + 1):
    solve()
