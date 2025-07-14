#https://usaco.org/index.php?page=viewproblem2&cpid=894
# -- Helpers --
import sys
import os

problem_name = "tamingtheherd"

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
field_num = read_int()
edge_counts = [0 for _ in range(field_num)]
for _ in range(field_num - 1):
    field1, field2 = [int(i) for i in read_ints()]
    edge_counts[field1-1] += 1
    edge_counts[field2-1] += 1

print(max(edge_counts) + 1)