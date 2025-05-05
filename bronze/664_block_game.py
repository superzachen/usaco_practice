# https://usaco.org/index.php?page=viewproblem2&cpid=664
# -- Helpers --
import sys
import os

problem_name = "blocks"

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
char_counts = [0] * 26

alphabet = "abcdefghijklmnopqrstuvwxyz"

for _ in range(N):
    word1, word2 = read_strs()
    
    freq1 = [word1.count(alphabet[i]) for i in range(26)]
    freq2 = [word2.count(alphabet[i]) for i in range(26)]
    
    for i in range(26):
        char_counts[i] += max(freq1[i], freq2[i])

for count in char_counts:
    print(count)