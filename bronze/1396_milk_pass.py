#https://usaco.org/index.php?page=viewproblem2&cpid=1396
# -- Helpers --
import sys
import os
import math

problem_name = "It's mooin Time III"

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
n, m = read_ints()
s = read_str()
a = read_ints()

total = sum(a)

for i in range(n):
    if s[i] == "R" and s[(i+1)%n] == "L":
        lostamount = 0
        left = (i-1)%n
        while s[left] == "R":
            lostamount += a[left]
            left = (left-1)%n
        total -= min(lostamount, m)
    if s[i] == "L" and s[(i-1)%n] == "R":
        lostamount = 0
        right = (i+1)%n
        while s[right] == "L":
            lostamount += a[right]
            right = (right+1)%n
        total -=  min(lostamount, m)
print(total)