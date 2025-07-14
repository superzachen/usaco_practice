#https://usaco.org/index.php?page=viewproblem2&cpid=810# -- Helpers --
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

#end of helpers
L, N, rF, rB = read_ints()
stops = [read_ints() for _ in range(N)]

stops.sort()

max_tastiness = 0
current_pos = 0
    
    
max_tastiness_so_far = 0
max_tastiness_stops = []
for i in range(N - 1, -1, -1):
    if stops[i][1] > max_tastiness_so_far:
        max_tastiness_so_far = stops[i][1]
        max_tastiness_stops.append(stops[i])
max_tastiness_stops.reverse()


for pos, tastiness in max_tastiness_stops:
    time_diff = (rF - rB) * (pos - current_pos)
    max_tastiness += time_diff * tastiness
    current_pos = pos

print(max_tastiness)