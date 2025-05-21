# -- Helpers --
import sys
import os

problem_name = "cbarn"

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
INF = float('inf')  # Define an infinite value for comparisons

def solve(me, other, dir, x, y):
    """
    Determines the time at which two cows may collide based on their movement direction.
    Returns (t1, t2) where:
      - t1 is the time the first cow reaches the intersection
      - t2 is the time the second cow reaches the intersection
      - If no collision occurs, returns (INF, INF)
    """
    if dir[me] == dir[other]:  # If both cows move in the same direction, they won't collide
        if dir[me] == 'N':  # Both are moving north
            if x[me] == x[other] and y[me] <= y[other]: 
                return 0, y[other] - y[me]  # One cow is ahead, so collision happens instantly
        else:  # Both are moving east
            if y[me] == y[other] and x[me] <= x[other]:
                return 0, x[other] - x[me]
        return INF, INF  # No collision occurs

    # If cows are moving in opposite directions
    if dir[me] == 'E':  # Cow 'me' is moving east, 'other' is moving north
        if x[other] > x[me] and y[other] <= y[me] and x[other] + y[other] > x[me] + y[me]:
            return y[me] - y[other], x[other] - x[me]
    else:  # Cow 'me' is moving north, 'other' is moving east
        if y[other] > y[me] and x[other] <= x[me] and x[other] + y[other] > x[me] + y[me]:
            return x[me] - x[other], y[other] - y[me]

    return INF, INF  # No valid intersection

# Read input
n = read_int()
dir, x, y = [], [], []

# Read cow data
for _ in range(n):
    d, xi, yi = read_strs()
    dir.append(d)
    x.append(int(xi))
    y.append(int(yi))

collisions = []  # Store potential collision events

# Compute all possible collisions between cows
for i in range(n):
    for j in range(n):
        if i == j:
            continue  # Skip checking a cow against itself
        t1, t2 = solve(i, j, dir, x, y)
        if t1 != INF:
            collisions.append((t1, t2, i, j))

# Sort collisions by earliest occurrence
collisions.sort()

# Initialize stopping times for each cow
ans = [INF] * n

# Process collisions in order
for t1, t2, cow1, cow2 in collisions:
    if ans[cow2] < t1:
        continue  # If cow2 already stopped before t1, skip
    ans[cow1] = min(ans[cow1], t2)  # Cow1 stops at the earliest collision time

# Print results
for i in range(n):
    print("Infinity" if ans[i] == INF else ans[i])