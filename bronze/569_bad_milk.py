# https://usaco.org/index.php?page=viewproblem2&cpid=569
# -- Helpers --
import sys
import os

problem_name = "billboard"

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
freinds, milks, D, S = read_ints()
events = []
for _ in range(D):
    e = [int(i) for i in read_ints()]
    e[0] -= 1
    e[1] -= 1
    events.append(tuple(e))

for _ in range(S):
    e = [int(i) for i in read_ints()]
    e[0] -= 1
    events.append((e[0], -1, e[1]))

events = sorted(events, key=lambda e: (e[0], e[2]))
dose_count = 0
for m in range(milks):
    is_bad = True
    can_be_sick = [False for _ in range(freinds)]
    for event in events:
        if event[1] == -1:
            if not can_be_sick[event[0]]:
                is_bad = False
                break
        elif event[1] == m:
            can_be_sick[event[0]] = True
    if is_bad:
        dose_count = max(dose_count, sum(can_be_sick))

print(dose_count)