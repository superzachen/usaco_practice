# https://cses.fi/problemset/task/1625
# -- Helpers --
import sys
import os

problem_name = "balancing"

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
dirR = [-1, 1, 0, 0]
dirC = [0, 0, -1, 1]

visited = [[0] * 9 for _ in range(9)]
for i in range(9):
    visited[0][i] = 1
    visited[8][i] = 1
    visited[i][0] = 1
    visited[i][8] = 1

directions = [-1] * 48
input = read_str()
for i in range(48):
    if input[i] == "U":
        directions[i] = 0

    if input[i] == "D":
        directions[i] = 1

    if input[i] == "L":
        directions[i] = 2

    if input[i] == "R":
        directions[i] = 3

def search(idx, R, C):
    #precheck
    if visited[R][C] == 1:
        return 0
    
    if idx == 48:
        if R == 7 and C == 1:
            return 1
        return 0
    elif R == 7 and C == 1:
        return 0
    
    # optimize, check if the current direction is spliting the board
    if visited[R + 1][C] and visited[R - 1][C] and visited[R][C-1] == 0 and visited[R][C+1] == 0:
        return 0
    if visited[R + 1][C] == 0 and visited[R - 1][C] == 0 and visited[R][C-1] and visited[R][C+1]:
        return 0

    dirsToGo = [0, 1, 2, 3]

    deadend_opt = 0
    # # optimization, avoid dead ends
    if visited[R - 1][C - 1] and visited[R - 1][C + 1] and visited[R - 1][C] == 0:
        dirsToGo = [0]
        deadend_opt += 1 
    elif visited[R + 1][C + 1] and visited[R - 1][C + 1] and visited[R][C + 1] == 0:
        dirsToGo = [3]
        deadend_opt += 1
    elif visited[R + 1][C + 1] and visited[R + 1][C - 1] and visited[R + 1][C] == 0:
        dirsToGo = [1]
        deadend_opt += 1
    elif visited[R + 1][C - 1] and visited[R - 1][C - 1] and visited[R][C - 1] == 0:
        dirsToGo = [2]
        deadend_opt += 1
    
    if deadend_opt > 1:
        return 0
    
    #If predifined
    if directions[idx] > -1:
        if len(dirsToGo) == 1 and dirsToGo[0] != directions[idx]:
            return 0
        dirsToGo = [directions[idx]]
    
    result = 0
    visited[R][C] = 1

    for dir in dirsToGo:
        newR = R + dirR[dir]
        newC = C + dirC[dir]
        result += search(idx + 1, newR, newC)

    # reset visited before return
    visited[R][C] = 0
    return result 

print(search(0, 1, 1))