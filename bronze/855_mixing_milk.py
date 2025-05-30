# -- Helpers --
import sys
import os

problem_name = "mixmilk"

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
cap1, buk1 = read_ints()
cap2, buk2 = read_ints()
cap3, buk3 = read_ints()

TURN_NUM = 100

for i in range(1, TURN_NUM + 1):
    if i % 3 == 1:
        amount_changed = min(buk1, cap2 - buk2)
        buk1 -= amount_changed
        buk2 += amount_changed
    if i % 3 == 2:
        amount_changed = min(buk2, cap3 - buk3)
        buk2 -= amount_changed
        buk3 += amount_changed
    if i % 3 == 0:
        amount_changed = min(buk3, cap1 - buk1)
        buk3 -= amount_changed
        buk1 += amount_changed


print(buk1)
print(buk2)
print(buk3)
