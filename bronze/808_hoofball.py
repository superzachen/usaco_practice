#https://usaco.org/index.php?page=viewproblem2&cpid=808
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
N = read_int()
cows = sorted(read_ints())
#print(cows)

def next_cow_index(cow_list, cow_index):
    if cow_index == 0:
        return 1
    elif cow_index == len(cow_list) - 1:
        return cow_index - 1
    else:
        left_side = cow_list[cow_index] - cow_list[cow_index - 1]
        right_side = cow_list[cow_index + 1] - cow_list[cow_index]
        if left_side <= right_side:
            return cow_index - 1
        elif right_side < left_side:
            return cow_index + 1

def test_cow(cow_index, cow_list, smallest, largest):
    cows_covered = set([cow_list[cow_index]])
    next_index = next_cow_index(cow_list, cow_index)
    while cow_list[next_index] not in cows_covered:
        cows_covered.add(cow_list[next_index])
        next_index = next_cow_index(cow_list, next_index)
    return sorted([i for i in cows_covered if smallest <= i <= largest])
    #return cows_covered


ball_count = 0
L = 0
R = N - 1
while L <= R:
    if L == R:
        ball_count += 1
        break
    cow_gaven_ball = 0
    most_covered = []
    for cow_idx in range(len(cows)):
        covered = test_cow(cow_idx, cows, cows[L], cows[R])
        if cows[L] not in covered and cows[R] not in covered:
            continue
        if len(covered) >= len(most_covered):
            cow_gaven_ball = cow_idx
            most_covered = covered

    #print(most_covered, cow_gaven_ball, cows[cow_gaven_ball])
    if most_covered[0] == cows[L]:
        L += len(most_covered)
    else:
        R -= len(most_covered)
    ball_count += 1

    
print(ball_count)