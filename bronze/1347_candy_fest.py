#https://usaco.org/index.php?page=viewproblem2&cpid=1347
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
    line =  sys.stdin.readline().split()
    return list(map(int, line))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()


# -- End of Helpers --
N, M = read_ints()
cows = read_ints()
candy_canes = read_ints()

def eat(cow_list, candy_cane):
    return_list = cow_list.copy()
    cur_candy_height = 0
    for i in range(len(cow_list)):
        if cow_list[i] > cur_candy_height:
            if cow_list[i] >= candy_cane:
                return_list[i] = (cow_list[i] + candy_cane-cur_candy_height)
                return return_list
            else:
                return_list[i] = (cow_list[i] + cow_list[i]-cur_candy_height)
            cur_candy_height = cow_list[i]
    return return_list

for candy in candy_canes:
    cows = eat(cows, candy)

for cow in cows:
    print(cow)
