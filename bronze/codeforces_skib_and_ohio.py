#https://codeforces.com/contest/2065/problem/B
# -- Helpers --
import sys
import os

problem_name = "cow_evo"

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
    line =  sys.stdin.readline().split()
    return list(map(int, line))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()


# -- End of Helpers --
def sim():
    str_input = read_str()
    for i in range(1, len(str_input)):
        if str_input[i - 1] == str_input[i]:
            print("1")
            return
    print(len(str_input))

t = read_int()
for _ in range(t):
    sim()