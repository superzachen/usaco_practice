#https://usaco.org/index.php?page=viewproblem2&cpid=784
# -- Helpers --
import sys
import os

problem_name = "lifeguards"

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

def find_total_time(ranges):
    farthest_point = 0
    closest_point = 0
    total_time = 0
    for range in ranges:
        if range[0] <= farthest_point:
            if range[1] > farthest_point:
                total_time += range[1] - farthest_point
                farthest_point = range[1]
        else:
            farthest_point = range[1]
            closest_point = range[0]
            total_time += farthest_point - closest_point
    return total_time

max_time = 0

shifts = []
for _ in range(N):
    shifts.append(tuple(read_ints()))

shifts = sorted(shifts)

for i in range(N):
    new_shifts = shifts[:i] + shifts[i + 1:]
    max_time = max(max_time, find_total_time(new_shifts))
    
print(max_time)
