#https://codeforces.com/contest/2044/problem/B
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
    return list(map(int, sys.stdin.readline().split()))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()


# -- End of Helpers --
N = read_int()
for _ in range(N):
    in_shop = []
    seen = read_str()
    for letter in seen:
        if letter == "q":
            in_shop.append("p")
        if letter == "p":
            in_shop.append("q")
        if letter == "w":
            in_shop.append("w")
    in_shop = list(reversed(in_shop))
    print(''.join(in_shop))
