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
N, M = read_ints()
data = [read_str() for _ in range(N)]
beat = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i):
        if data[i][j] != "D":
            if data[i][j] == "W":
                beat[i][j] = 1
            else:
                beat[j][i] = 1

for _ in range(M):
    x_str, y_str = read_ints()
    x = int(x_str) - 1
    y = int(y_str) - 1

    winning = 0
    for b in range(N):
        if beat[b][x] and beat[b][y]:
            winning += 1

    total_playable_pairs = N * N
    losing_pairs = (N - winning) * (N - winning)

    print(total_playable_pairs - losing_pairs)