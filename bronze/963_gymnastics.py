# https://usaco.org/index.php?page=viewproblem2&cpid=963
# -- Helpers --
import sys
import os

problem_name = "gymnastics"

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
K, N = read_ints()
pairs = set()
for _ in range(K):
    row = read_ints()
    if _ == 0:
        for i in range(N):
            for j in range(i + 1, N):
                pairs.add((row[i], row[j]))
    else:
        for i in range(N):
            for j in range(i + 1, N):
                if ((row[j], row[i])) in pairs:
                    pairs.remove((row[j], row[i]))
print(len(pairs))