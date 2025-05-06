# https://usaco.org/index.php?page=viewproblem2&cpid=987
# -- Helpers --
import sys
import os

problem_name = "word"

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
words = read_strs()
    
current_line_length = 0
result = []
current_line = []
    
for word in words:
    if current_line_length + len(word) <= k:
        current_line.append(word)
        current_line_length += len(word)
    else:
        result.append(" ".join(current_line))
        current_line = [word]
        current_line_length = len(word)
    
result.append(" ".join(current_line))
    
for line in result:
    print(line)