# https://usaco.org/index.php?page=viewproblem2&cpid=941
# -- Helpers --
import sys
import os

problem_name = "cow_evo"

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
cows = []
all_chars = set()
for _ in range(n):
    chars = set(read_strs()[1:])
    cows.append(chars)
    all_chars.update(chars)

all_chars = list(all_chars)

for a in range(len(all_chars)):
    for b in range(a + 1, len(all_chars)):
        both, only_a, only_b = False, False, False
        for c in cows:
            has_a = all_chars[a] in c
            has_b = all_chars[b] in c

            if has_a and has_b:
                both = True
            elif has_a and not has_b:
                only_a = True
            elif has_b and not has_a:
                only_b = True

        if only_a and only_b and both:
            print("no")
            exit()

print("yes")
