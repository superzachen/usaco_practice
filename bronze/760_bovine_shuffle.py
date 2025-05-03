# https://usaco.org/index.php?page=viewproblem2&cpid=760
# -- Helpers --
import sys
import os

problem_name = "shuffle"

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
cow_count = read_int()
order = read_ints()
ids = read_ints()
orignal_order = []
for _ in range(3):
    for i in range(cow_count):
        orignal_order.append(ids[order[i]-1])
    ids = orignal_order
    orignal_order = []
for id in ids:
    print(id)