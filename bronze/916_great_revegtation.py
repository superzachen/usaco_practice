# https://usaco.org/index.php?page=viewproblem2&cpid=916
# -- Helpers --
import sys
import os

problem_name = "greatrevegtation"

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
N, M = read_ints()
cows_fav = []
for _ in range(M):
    p1, p2 = sorted(read_ints())
    cows_fav.append((p1 - 1, p2 - 1))

pastures = [1] * N

cows_fav.sort()
for c, (a, b) in enumerate(cows_fav):
    if pastures[a] != pastures[b]:
        continue

    pastures[b] += 1

    for i, j in cows_fav[:c]:
        if pastures[i] == pastures[j]:
            pastures[j] += 1

print(int("".join(map(str, pastures))))