# https://usaco.org/index.php?page=viewproblem2&cpid=1012
# -- Helpers --
import sys
import os

problem_name = "breedflip"

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
def count_flips(before, after):
    n = len(before)
    flips = 0
    i = 0
    
    while i < n:
        if before[i] != after[i]:
            flips += 1
        i += 1
            
    
    return flips + 1

before = read_strs()
after = read_strs()
print(count_flips(before, after)) 