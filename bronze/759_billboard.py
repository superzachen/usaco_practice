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
def area(x1, y1, x2, y2):
    return max(0, (x2 - x1)) * max(0, (y2 - y1))

def overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    return area(max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))

x1, y1, x2, y2 = read_ints()
x3, y3, x4, y4 = read_ints()
x5, y5, x6, y6 = read_ints()

area1 = area(x1, y1, x2, y2)
area2 = area(x3, y3, x4, y4)

covered1 = overlap(x1, y1, x2, y2, x5, y5, x6, y6)
covered2 = overlap(x3, y3, x4, y4, x5, y5, x6, y6)

visible_area = (area1 - covered1) + (area2 - covered2)

print(visible_area)