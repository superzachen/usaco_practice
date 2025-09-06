#https://usaco.org/index.php?page=viewproblem2&cpid=1517
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
n, q = read_ints()
s = read_str()

for _ in range(q):
    l, r = read_ints()
    moosum = -1
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            if s[i - 1] == s[j - 1]:
                continue
            for k in range(j + 1, r + 1):
                if s[j - 1] == s[k - 1]:
                    moosum = max(moosum, (j - i) * (k - j))
    print(moosum)