#https://codeforces.com/contest/2044/problem/C
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
N = read_int()
for _ in range(N):
    m, a, b, c = read_ints()
    preferred_seated = min(a, m) + min(b, m)
    remaining_seats = max(0, m - a) + max(0, m - b)
    flexible_seated = min(c, remaining_seats)
    total_monkeys_seated = preferred_seated + flexible_seated
    print(total_monkeys_seated)