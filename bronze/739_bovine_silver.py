# https://usaco.org/index.php?page=viewproblem2&cpid=739
# -- Helpers --
import sys
import os

problem_name = "cownomics"

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

N, M = read_ints()
answer = 0
dnas = []
for _ in range(N * 2):
    dnas.append(read_str())
    
s = set()
for pos in itertools.combinations(range(M), 3):
    s.clear()
    good = True
    for i in range(N):
        dna = dnas[i]
        s.add((dna[pos[0]], dna[pos[1]], dna[pos[2]]))
    for i in range(N):
        dna = dnas[i + N]
        if (dna[pos[0]], dna[pos[1]], dna[pos[2]]) in s:
            good = False
            break
    if good:
        answer += 1
print(answer)
