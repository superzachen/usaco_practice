#https://usaco.org/index.php?page=viewproblem2&cpid=1469
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
N = read_int()
A = read_ints()
B = read_ints()
def checkup_count(A, B):
    answer = 0
    for i in range(N):
        if A[i] == B[i]:
            answer += 1
    return answer
for i in range(N + 1):
    answer = 0
    for j in range(len(A)):
        for x in range(j, len(A)):
            temp_a = A.copy()
            temp_a[j:x + 1] = temp_a[j:x + 1][::-1]
            #print(j, x, A, temp_a)
            if i == checkup_count(temp_a, B):
                answer += 1
    print(answer)