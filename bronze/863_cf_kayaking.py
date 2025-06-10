# https://codeforces.com/contest/863/problem/B
# -- Helpers --
import sys
import os

problem_name = "gymnastics"

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
weights.sort()
min_instability = float('inf')
    
for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        temp_weights = []
        for k in range(2 * n):
            if k != i and k != j:
                temp_weights.append(weights[k])
        instability = 0
        for k in range(0, len(temp_weights), 2):
            instability += abs(temp_weights[k] - temp_weights[k+1])
        min_instability = min(min_instability, instability)
print(min_instability)