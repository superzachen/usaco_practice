# https://usaco.org/index.php?page=viewproblem2&cpid=592
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
N = read_int()
haybales = [read_int() for _ in range(N)]

def explode(haybales, i):
    not_destroyed = set(haybales)
    next_to_explode = [i]
    not_destroyed.remove(i)
    t = 1
    while len(next_to_explode) > 0:
        new_to_explode = []
        for i in not_destroyed:
            for j in next_to_explode:
                if abs(j - i) <= t:
                    new_to_explode.append(i)
                    break
        t += 1
        for i in new_to_explode:
            not_destroyed.remove(i)
        next_to_explode = new_to_explode
    return len(haybales) - len(not_destroyed)


result = 0
for h in haybales:
    result = max(result, explode(haybales, h))
print(result)