# https://usaco.org/index.php?page=viewproblem2&cpid=1059
# -- Helpers --
import sys
import os

problem_name = "billboard"

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
nums = sorted(read_ints())

# A and B are the smallest numbers
a, b = nums[0], nums[1]

# C is found using the largest number, which represents A + B + C
c = nums[6] - a - b

# Print the values of A, B, and C
print(a, b, c)