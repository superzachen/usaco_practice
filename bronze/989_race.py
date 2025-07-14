#https://usaco.org/index.php?page=viewproblem2&cpid=989
# -- Helpers --
import sys
import os

problem_name = "tamingtheherd"

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


s_cache = dict()
sum_cache = dict()
ok_cache = dict()

def S(n):
    if n in s_cache:
        return s_cache[n]
    # sum of 1....n
    result = n * (n + 1) // 2
    s_cache[n] = result
    return result

def sum_(A, B):
    if (A, B) in sum_cache:
        return sum_cache[(A, B)]
    # sum of A...B
    result = S(B) - S(A - 1) if A <= B else 0
    sum_cache[(A, B)] = result
    return result

def ok(speed, final_speed, L):
    if (speed, final_speed, L) in ok_cache:
        return ok_cache[(speed, final_speed, L)]
    result = speed <= final_speed or (sum_(final_speed + 1, speed - 1) + 1 <= L)
    ok_cache[(speed, final_speed, L)] = result
    return result

def solve(left, final_speed):
    cur_speed, t = 0, 0

    while left > 0:
        if ok(cur_speed + 1, final_speed, left - (cur_speed + 1)):
            cur_speed += 1
        elif not ok(cur_speed, final_speed, left - cur_speed):
            cur_speed -= 1

        left -= cur_speed
        t += 1

    return t

k, n = read_ints()
X = [read_int() for _ in range(n)]

for x in X:
    print(solve(k, x))
    