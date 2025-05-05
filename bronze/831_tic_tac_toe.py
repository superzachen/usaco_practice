# https://usaco.org/index.php?page=viewproblem2&cpid=831
# -- Helpers --
import sys
import os

problem_name = "tttt"

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
board = [read_str() for _ in range(3)]  

solo_winners, team_winners = set(), set()  

def check_winner(row, collum, directionr, directionc):  
    players = set()  
    for i in range(3):  
        players.add(board[row + i * directionr][collum + i * directionc])  
    
    if len(players) == 1:  
        solo_winners.add(players.pop())  
    elif len(players) == 2:  
        team_winners.add(tuple(players))  

for i in range(3):  
    check_winner(i, 0, 0, 1)
    check_winner(0, i, 1, 0)

check_winner(0, 0, 1, 1)
check_winner(0, 2, 1, -1)

print(len(solo_winners))  
print(len(team_winners))  