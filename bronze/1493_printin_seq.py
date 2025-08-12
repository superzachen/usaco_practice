#https://usaco.org/index.php?page=viewproblem2&cpid=1493
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
def solve1(l):
    if len(l) == 0:
        return True
    return min(l) == max(l)


def solve2(l):
    if solve1(l):
        return True
    r = 0
    blocks = []
    while r < len(l):
        i = r
        while r < len(l) and l[r] == l[i]:
            r += 1
        blocks.append((r - i, l[i]))
    return len(blocks) % 2 == 0 and blocks[2:] == blocks[:-2]


def solve3(l):
    for i in range(1, len(l) + 1):
        if len(l) % i == 0:
            if l[:-len(l) // i] == l[len(l) // i:]:
                substring = l[:len(l) // i]
                for i in range(len(substring) + 1):
                    if solve2(substring[:i]) and solve1(substring[i:]):
                        return True
                    if solve1(substring[:i]) and solve2(substring[i:]):
                        return True


def solve():
    N, K = read_ints()
    seq = read_ints()
    if K == 1:
        return solve1(seq)
    elif K == 2:
        return solve2(seq)
    else:
        assert K == 3
        return solve3(seq)


T = read_int()
for _ in range(T):
    print("YES" if solve() else "NO")