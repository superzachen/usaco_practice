# https://usaco.org/index.php?page=viewproblem2&cpid=939
# -- Helpers --
import sys
import os

problem_name = "buckets"

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
for i in range(10):
    row = read_str()
    for j in range(10):
        if row[j] == "B":
            barn_x = i
            barn_y = j
        if row[j] == "R":
            rock_x = i
            rock_y = j
        if row[j] == "L":
            lake_x = i
            lake_y = j
	# distance without accounting for the rock
cow_count = abs(barn_x - lake_x) + abs(barn_y - lake_y) - 1# This is because the cow doesn't start on the barn

# Row Check
if barn_x == rock_x == lake_x and (
	lake_y < rock_y < barn_y or barn_y < rock_y < lake_y
):
	cow_count += 2

# column check
elif barn_y == rock_y == lake_y and (
	lake_x < rock_x < barn_x or barn_x < rock_x < lake_x
):
	cow_count += 2
print(cow_count)