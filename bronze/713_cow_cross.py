#https://usaco.org/index.php?page=viewproblem2&cpid=713
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
N = read_int()

# Store cow data (arrival_time, duration)
cows = [read_ints() for _ in range(N)]

# Sort cows by arrival time
cows.sort()

current_time = 0

# Process cows one by one
for arrival, duration in cows:
    # Wait if necessary
    current_time = max(current_time, arrival)
    current_time += duration
print(current_time)
