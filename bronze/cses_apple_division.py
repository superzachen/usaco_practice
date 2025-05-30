# https://cses.fi/problemset/task/1623/
# -- Helpers --
import sys
import os

problem_name = "balancing"

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
n = read_int()
weights = read_ints()
def find_min_diff(i, sum1, sum2):
    if i == n:
        return abs(sum2 - sum1)
            
    diff1 = find_min_diff(i + 1, sum1 + weights[i], sum2)
    diff2 = find_min_diff(i + 1, sum1, sum2 + weights[i])
        
    return min(diff1, diff2)
    

if n == 0:
    print(0)
else:
    result = find_min_diff(0, 0, 0)
    print(result)