#https://codeforces.com/contest/2094/problem/C
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
def solve():
    n = read_int()
    ans = [0] * (2 * n + 1)
    used = [False] * (2 * n + 1)
    
    for i in range(1, n + 1):
        x = read_ints()
        for j in range(n):
            ans[i + j + 1] = x[j]
            used[x[j]] = True
            
    for i in range(1, 2 * n + 1):
        if ans[i] != 0:
            print(ans[i], end=" ")
        else:
            for j in range(1, 2 * n + 1):
                if not used[j]:
                    used[j] = True
                    print(j, end=" ")
                    break
    print()

t = read_int()
for _ in range(t):
    solve()