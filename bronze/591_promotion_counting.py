# https://usaco.org/index.php?page=viewproblem2&cpid=591
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
bronze = read_ints() # Not used
silver = read_ints()
gold = read_ints()
platinum = read_ints()

platinum_promo = platinum[1] - platinum[0]
gold_promo = platinum_promo + gold[1] - gold[0]
silver_promo = gold_promo + silver[1] - silver[0]
print(silver_promo)
print(gold_promo)
print(platinum_promo)