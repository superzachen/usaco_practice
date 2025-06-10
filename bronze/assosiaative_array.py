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
q = read_int()
mp = {}
for _ in range(q):
    input = read_ints()
    type_ = input[0]
    key = input[1]
    if len(input) == 3:
        val = input[2]
    if type_ == 0:
        mp[key] = val
    else:
        print(mp.get(key, 0))
