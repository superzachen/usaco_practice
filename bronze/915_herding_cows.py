# https://usaco.org/index.php?page=viewproblem2&cpid=915
# -- Helpers --
import sys
import os

problem_name = "herding"

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
nums = list(read_ints())
if nums[0] + 2 == nums[2]:
    print(0)
elif nums[1] == nums[0] + 2 or nums[2] == nums[1] + 2:
    print(1)
else:
    print(2)
print(max(nums[1] - nums[0], nums[2] - nums[1]) - 1)# measures the largest gap, and subtractes 1 because we moving inside, so there is 1 less step.
