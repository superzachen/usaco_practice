# -- Helpers --
import sys
import os
import math

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
t = read_int()
for _ in range(t):
    a1, a2, b1, b2 = read_ints()
    suneet_cards = [a1, a2]
    slavic_cards = [b1, b2]
    
    from itertools import permutations
    win_count = 0
    
    for s_order in permutations(suneet_cards):
        for l_order in permutations(slavic_cards):
            s_wins = 0
            l_wins = 0
            for s_card, l_card in zip(s_order, l_order):
                if s_card > l_card:
                    s_wins += 1
                elif s_card < l_card:
                    l_wins += 1
            if s_wins > l_wins:
                win_count += 1
    print(win_count)