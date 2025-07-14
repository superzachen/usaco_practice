#https://codeforces.com/contest/2044/problem/D
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
index = 0
tt = read_int()
index += 1

for _ in range(tt):
    n = read_int()
    index += 1
    a = [False] * (n + 1)
    b = [0] * n
    unused = []

    X = read_ints()

    # Track used numbers and build b
    for i, x in enumerate(X):
        index += 1
        if not a[x]:
            b[i] = x
            a[x] = True

    # Collect unused values
    unused = [i for i in range(1, n + 1) if not a[i]]
    unused_idx = 0

    # Fill remaining b values
    for i in range(n):
        if b[i] == 0:
            b[i] = unused[unused_idx]
            unused_idx += 1

    print(" ".join(map(str, b)))