#https://usaco.org/index.php?page=viewproblem2&cpid=940
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
station_num = read_int()
outgoing = [0 for _ in range(station_num)]
for _ in range(station_num - 1):
    s1, s2 = [int(i) - 1 for i in read_ints()]
    outgoing[s1] += 1

no_outs = []
for s in range(station_num):
	if outgoing[s] == 0:
		no_outs.append(s + 1)

answer_station = no_outs[0] if len(no_outs) == 1 else -1
print(answer_station)