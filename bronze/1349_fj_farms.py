# https://usaco.org/index.php?page=viewproblem2&cpid=1349
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
    line = sys.stdin.readline().split()
    return list(map(int, line))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()


# -- End of Helpers --
def find_working_day(init1, init2, growth1, growth2, cur_day):
    height1 = init1 + cur_day * growth1
    height2 = init2 + cur_day * growth2
    if growth1 <= growth2 and height1 <= height2:
        return -1
    if height1 > height2:
        return cur_day
    distance = height2 - height1
    delta_speed = growth1 - growth2
    extra_days = (distance + delta_speed) // delta_speed
    return cur_day + extra_days

def simulate_1_testcase(N):
    if N == 1:
        return 0
    curr_day = 0
    for i in range(N - 1):
        j = i + 1
        
        initial1 = start_height[i]
        initial2 = start_height[j]
        growth1 = growth[i]
        growth2 = growth[j]
        new_day = find_working_day(initial1, initial2, growth1, growth2, curr_day)
        #print(new_day, idx1, idx2, initial1, initial2, growth1, growth2)
        if new_day == -1:
            return -1
        else:
            curr_day = new_day
    for i in range(N - 1):
        j = i + 1
        heighti = start_height[i] + curr_day*growth[i]
        heightj = start_height[j] + curr_day*growth[j]
        if heighti <= heightj:
            return -1
    return curr_day


t = read_int()
for _ in range(t):
    N = read_int()
    start_height = read_ints()
    growth = read_ints()
    ordering = read_ints()
    new_start_height = [0] * N
    new_growth = [0] * N
    for i in range(N):
        o = ordering[i]
        new_start_height[o] = start_height[i]
        new_growth[o] = growth[i]
    start_height = new_start_height
    growth = new_growth
    #print(start_height, growth, ordering)
    print(simulate_1_testcase(N))
