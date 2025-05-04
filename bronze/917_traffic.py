# https://usaco.org/index.php?page=viewproblem2&cpid=917
# -- Helpers --
import sys
import os

problem_name = "traffic"

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
segments = []
for _ in range(N):
    segments.append(read_strs())

lower_bound_before = 0
upper_bound_before = 1000
lower_bound_after = 0
upper_bound_after = 1000

for segment in segments:
    type = segment[0]
    lower = int(segment[1])
    upper = int(segment[2])

    if type == "none":
        lower_bound_after = max(lower_bound_after, lower)
        upper_bound_after = min(upper_bound_after, upper)
    elif type == "on":
        lower_bound_after += lower
        upper_bound_after += upper
    elif type == "off":
        lower_bound_after -= upper
        upper_bound_after -= lower

for segment in reversed(segments):
    type = segment[0]
    lower = int(segment[1])
    upper = int(segment[2])

    if type == "none":
        lower_bound_before = max(lower_bound_before, lower)
        upper_bound_before = min(upper_bound_before, upper)
    elif type == "off":
        lower_bound_before += lower
        upper_bound_before += upper
    elif type == "on":
        lower_bound_before -= upper
        upper_bound_before -= lower

print(max(0, lower_bound_before), upper_bound_before)
print(max(0,lower_bound_after), upper_bound_after)
