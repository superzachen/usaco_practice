#https://usaco.org/index.php?page=viewproblem2&cpid=689
# -- Helpers --
import sys
import os

problem_name = "tamingtheherd"

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
cows = [[int(c) for c in read_str()]  for _ in range(N)]
R = N - 1
C = R
answer = 0
one_count = 0
for row in cows:
    one_count += sum(row)

def flip(onecount, cows, r, c):
    for i in range(r + 1):
        for j in range(c + 1):
            if cows[i][j]:
                cows[i][j] = 0
                onecount -= 1
            else:
                cows[i][j] = 1
                onecount += 1
    return onecount


while one_count:
    #print(R, C, one_count, answer)
    if cows[R][C] == 1:
        one_count = flip(one_count, cows, R, C)
        answer += 1
    if C != 0:
        C -= 1
    elif C == 0:
        R -= 1
        C = N - 1



print(answer)