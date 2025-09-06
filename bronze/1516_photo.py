#https://usaco.org/index.php?page=viewproblem2&cpid=1516
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
t = read_int()
for _ in range(t):
    n = read_int()
    Heights = read_ints()
    freq = {}
    for h in Heights:
        if h in freq:
            freq[h] += 1
        else:
            freq[h] = 1

    max_height = max(freq.keys())
    pairs = 0
    for h in freq:
        if freq[h] >= 2:
            pairs += 1
    result = 2 * pairs
    if freq[max_height] == 1:
        result += 1
    elif freq[max_height] >= 2:
        result -= 1 
    print(result)