# https://usaco.org/index.php?page=viewproblem2&cpid=965
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
import itertools


N = read_int()

def find_restraints(line):
    words = line.split()
    cow = words[0]
    next_to = words[-1]
    return cow, next_to

restraints = []
for _ in range(N):
    restraints.append(find_restraints(read_str()))

cows = ["Beatrice", "Bella", "Belinda", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]

def valid_order(order, restraints):
    for cow1, cow2 in restraints:
        if abs(order.index(cow1) - order.index(cow2)) != 1:
            return False
    return True

def find_possible_outcomes(restraints):
    valid_orders = []
    for perm in itertools.permutations(cows):
        if valid_order(perm, restraints):
            valid_orders.append(perm)
    return valid_orders

results = find_possible_outcomes(restraints)
results = sorted(results)
for r in results[0]:
    print(r)