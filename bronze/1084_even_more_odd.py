#https://usaco.org/index.php?page=viewproblem2&cpid=1084
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
def group(odd, even):
    diff = odd - even
    if diff == 0:
        return odd + even
    elif diff == 1:
        return odd + even - 2
    elif diff == 2:
        return even + odd - 1
    else:
        odd -= 2
        even += 1

    return group(odd, even)

N = read_int()
cows = read_ints()
oddC = 0
evenC = 0
for cow in cows:
    if cow % 2 == 0:
        evenC += 1
    else:
        oddC += 1   

if evenC > oddC:
    print(2 * oddC + 1)
else:
    print(group(oddC, evenC))
