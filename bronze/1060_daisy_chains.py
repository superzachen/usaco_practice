#https://usaco.org/index.php?page=viewproblem2&cpid=1060
# -- Helpers --
import sys
import os
import math

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
petals = read_ints()
photos = 0
    
for i in range(n):
    present = [False] * 1001
    petals_seen = 0
        
    for j in range(i, n):
        petals_seen += petals[j]
        present[petals[j]] = True
            
        if petals_seen % (j - i + 1) == 0 and present[petals_seen // (j - i + 1)]:
            photos += 1
                
print(photos)