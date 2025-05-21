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
x5, y5, x6, y6 = read_ints()

span = (max(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6) + 1) * 2


visible = [[False for _ in range(span)] for _ in range(span)]
x1 += span // 2
y1 += span // 2
x2 += span // 2
y2 += span // 2
x3 += span // 2
y3 += span // 2
x4 += span // 2
y4 += span // 2
x5 += span // 2
y5 += span // 2
x6 += span // 2
y6 += span // 2
for x in range(x1, x2):
	for y in range(y1, y2):
		visible[x][y] = True
for x in range(x3, x4):
	for y in range(y3, y4):
		visible[x][y] = True
for x in range(x5, x6):
	for y in range(y5, y6):
		visible[x][y] = False



answer = 0
for x in range(span):
	for y in range(span):
		answer += visible[x][y]
print(answer)