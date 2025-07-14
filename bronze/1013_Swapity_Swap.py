#https://usaco.org/index.php?page=viewproblem2&cpid=1013
# -- Helpers --
import sys
import os

problem_name = "swapity_swap"

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
def nex(x, A1, A2, B1, B2):
    if A1 <= x <= A2:  # simulate step 1
        x = A1 + A2 - x
    if B1 <= x <= B2:  # simulate step 2
        x = B1 + B2 - x
    return x

N, K = read_ints()
A1, A2 = read_ints()
B1, B2 = read_ints()

result = [0] * (N + 1)
for i in range(1, N + 1):
    p = 1
    cur = nex(i, A1, A2, B1, B2)
    while cur != i:
        p += 1
        cur = nex(cur, A1, A2, B1, B2) 
    k = K % p
    for _ in range(k):
        cur = nex(cur, A1, A2, B1, B2)
    result[cur] = i 
for i in range(1, N + 1):
    print(result[i])

