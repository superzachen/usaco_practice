#https://usaco.org/index.php?page=viewproblem2&cpid=1467
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
def solve(N, A, B, pixels):
    if A == 0 and B == 0:
        answer = 0
        for r in range(N):
            line = pixels[r]
            for c in range(N):
                if line[c] != "W":
                    answer += 1
        return(answer)
    else:
        answer = 0
        for r in range(N):
            for c in range(N):
                old_R = r - B
                old_C = c - A
                new_R = r + B
                new_C = c + A
                cur_p = pixels[r][c]
                pre_out_bound = old_R < 0 or old_R >= N or old_C < 0 or old_C >= N
                next_out_bound = new_R < 0 or new_R >= N or new_C < 0 or new_C >= N
                if cur_p == 'B':
                    if pre_out_bound or pixels[old_R][old_C] == "W":
                        return -1
                    answer += 1
                elif cur_p == 'G':
                    # check out of bound
                    if pre_out_bound:
                        answer += 1
                    elif not next_out_bound and pixels[new_R][new_C] == 'B':
                        answer += 1
                    elif not pre_out_bound and pixels[old_R][old_C] == "W":
                        answer += 1
                    elif pixels[old_R][old_C] == "G" or "B":
                        pixels[r][c] = "W"
    return answer       

            

t = read_int()
for _ in range(t):
    N, A, B = read_ints()
    pixels = []
    for _ in range(N):
        pixels.append(list(read_str()))
    print(solve(N, A, B, pixels))
