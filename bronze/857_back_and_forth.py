# http://usaco.org/index.php?page=viewproblem2&cpid=857
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
bucket1 = read_ints()
bucket2 = read_ints()
distinct_amounts = set()

def simulate_day(b1, b2, day):
    # Final Day
    if day == 4:
        distinct_amounts.add(sum(b2))
        return

    if day % 2 == 0: # Transfer from bucket 1 to bucket 2
        for i in range(len(b1)):
            temp1 = b1[:]
            temp2 = b2[:]
            temp2.append(temp1.pop(i))
            simulate_day(temp1, temp2, day+1)
    else: # Transfer from bucket 2 to bucket 1
        for i in range(len(b2)):
            temp1 = b1[:]
            temp2 = b2[:]
            temp1.append(temp2.pop(i))
            simulate_day(temp1, temp2, day+1)


simulate_day(bucket1, bucket2, 0)
print(len(distinct_amounts))