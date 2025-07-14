#https://codeforces.com/contest/2094/problem/D
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
def is_valid_sound(p, s):
    i = j = 0
    while i < len(p) and j < len(s):
        if s[j] != p[i]:
            return False
        j += 1
        if j < len(s) and s[j] == p[i]:  # Double sound
            j += 1
        i += 1
    return i == len(p) and j == len(s)

t = read_int()
for _ in range(t):
    p = read_str()
    s = read_str()
    print("YES" if is_valid_sound(p, s) else "NO")