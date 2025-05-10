# https://usaco.org/index.php?page=viewproblem2&cpid=593
# -- Helpers --
import sys
import os

problem_name = "blocks"

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
n = read_int()
moves = []
for _ in range(n):
    direction, steps = read_strs()
    moves.append((direction, int(steps)))

visited = set()
x, y = 0, 0
visited.add((x, y))
time = 0
earliest_revisit = -1

for direction, steps in moves:
    for _ in range(steps):
        time += 1
        if direction == 'N':
            y += 1
        elif direction == 'E':
            x += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'W':
            x -= 1

        if (x, y) in visited:
            earliest_revisit = time
            break
        visited.add((x, y))
    if earliest_revisit != -1:
        break

print(earliest_revisit)