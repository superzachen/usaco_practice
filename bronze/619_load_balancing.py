# https://usaco.org/index.php?page=viewproblem2&cpid=619
# -- Helpers --
import sys
import os

problem_name = "balancing"

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

x_value = []
y_value = []
x_fences = set()
y_fences = set()
for n in range(N):
    x, y = [i for i in read_ints()]
    x_value.append(x)
    y_value.append(y)
    x_fences.add(x + 1)
    y_fences.add(y + 1)


r = min((3 * N) // 4, N - 1)
x_fences = sorted(x_fences)[N // 4: r + 1]
y_fences = sorted(y_fences)[N // 4: r + 1]

M = 999999

for v in x_fences:
    for h in y_fences:
        top_left = 0
        top_right = 0
        bottom_left = 0
        bottom_right = 0
        for c in range(N):
            is_left = x_value[c] < v
            is_bottom = y_value[c] < h
            if is_left:
                if is_bottom:
                    bottom_left += 1
                else:
                    top_left += 1
            else:
                if is_bottom:
                    bottom_right += 1
                else:
                    top_right += 1
        M = min(M, max(top_left, top_right, bottom_left, bottom_right))

print(M)
