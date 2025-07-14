#https://usaco.org/index.php?page=viewproblem2&cpid=785
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
cow_num = read_int()
cows = [read_int() for _ in range(cow_num)]

sorted_order = sorted(cows)

# The number of cows that are out of place relative to the sorted order
answer = 0
for i in range(len(cows)):
	if cows[i] != sorted_order[i]:
		answer += 1
print(answer - 1)