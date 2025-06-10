# https://usaco.org/index.php?page=viewproblem2&cpid=809
# -- Helpers --
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


# -- End of Helpers --
N = read_int()
logs = read_ints()
logs[0] = 0
works = True
for i in range(N - 1, -1, -1):
    if logs[i] != -1:
        for j in range(logs[i] + 1):
            if i - j >= 0:
                if logs[i - j] == -1 or logs[i - j] == logs[i] - j:
                    logs[i - j] = logs[i] - j
                else:
                    print(-1)
                    exit()

if works:
    add_on = 0
    minimum = 0
    for i in logs:
        if i == 0:
            minimum += 1
        elif i == -1:
            add_on += 1
    print(minimum, minimum + add_on)