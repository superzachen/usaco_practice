#https://usaco.org/index.php?page=viewproblem2&cpid=988
# -- Helpers --
import sys
import os

problem_name = "photo"

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
    line = sys.stdin.readline().split()
    return list(map(int, line))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()


# -- End of Helpers --
def solve_photoshoot(N, B):
    # Try every possible value for a[0]
    for first in range(1, N + 1):
        A = [first]
        used = set(A)
        valid = True

        # Reconstruct the rest of A
        for i in range(N - 1):
            next_val = B[i] - A[i]
            # Check validity of next value
            if 1 <= next_val <= N and next_val not in used:
                A.append(next_val)
                used.add(next_val)
            else:
                valid = False
                break

        if valid:
            return A
n = read_int()
b = read_ints()
print(" ".join(map(str, solve_photoshoot(n, b))))