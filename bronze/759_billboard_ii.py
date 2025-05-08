# https://usaco.org/index.php?page=viewproblem2&cpid=759
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
x1, y1, x2, y2 = read_ints()
x3, y3, x4, y4 = read_ints()

ax1 = x1
ay1 = y1
ax2 = x2
ay2 = y2


if x3 < x1 < x4 < x2 and y4 > y2 and y3 < y1:
    ax1 = x4
if y3 < y1 < y4 < y2 and x3 < x1 and x2 < x4:
    ay1 = y4
if x1 < x3 < x2 < x4 and y4 > y2 and y3 < y1:
    ax2 = x3
if y1 < y3 < y2 < y4 and x3 < x1 and x2 < x4:
    ay2 = y3
if y3 <= y1 <= y2 <= y4 and x3 <= x1 and x2 <= x4:
    ax1 = ax2



print((ax2 - ax1) * (ay2 - ay1))