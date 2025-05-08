# https://usaco.org/index.php?page=viewproblem2&cpid=639
# -- Helpers --
import sys
import os

problem_name = "diamond"

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
n, k = read_ints()
diamonds = []
for _ in range(n):
    diamonds.append(read_int())
diamonds.sort()
    
max_count = 0
for i in range(n):
    count = 0
    for j in range(n):
        if diamonds[j] >= diamonds[i] and diamonds[j] <= diamonds[i] + k:# Check if the diamonds can be put in same box
            count += 1
    max_count = max(0, count)
    
print(max_count)
