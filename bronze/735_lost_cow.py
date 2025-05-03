# https://usaco.org/index.php?page=viewproblem2&cpid=735
# -- Helpers --
import sys
import os

problem_name = "lostcow"

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
J, C = read_ints()
orginalpos = J
total_distance = 0
travel_distance = 1

if J == C:
    print(0)
else:
    while True:
        total_distance += abs(J - (orginalpos + travel_distance))
        J = orginalpos + travel_distance
        travel_distance *= -2
        if orginalpos < C and J > C or orginalpos > C and J < C or J == C:
            total_distance -= abs(J-C)
            break

    print(total_distance)