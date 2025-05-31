# https://usaco.org/index.php?page=viewproblem2&cpid=360
# -- Helpers --
import sys
import os

problem_name = "wormhole"

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
wormholes = [read_ints() for _ in range(N)]
# print(wormholes)


def get_next_on_right(holes):
    next_on_right = [-1] * N
    for i in range(N):
        for j in range(N):
            if holes[j][0] > holes[i][0] and holes[i][1] == holes[j][1]:
                if (
                    next_on_right[i] == -1
                    or holes[j][0] - holes[i][0]
                    < holes[next_on_right[i]][0] - holes[i][0]
                ):
                    next_on_right[i] = j
    return next_on_right


def get_pairings(holes):
    if not holes:
        yield []
        return

    first = holes[0]
    others = holes[1:]
    for i in range(len(others)):
        pair = (first, others[i])
        remaining_elements = others[:i] + others[i + 1 :]
        for pairings in get_pairings(remaining_elements):
            yield [pair] + pairings


def pairings_to_mappings(parings):
    result = []
    for paring in parings:
        mapping = [0] * len(paring) * 2
        for p in paring:
            mapping[p[0]] = p[1]
            mapping[p[1]] = p[0]
        result.append(mapping)
    return result


parings = list(get_pairings(list(range(N))))
mappings = pairings_to_mappings(parings)
next_on_right = get_next_on_right(wormholes)

answer = 0

def detect_cycle(the_mapping, the_next_on_right):
    for i in range(N):
        in_hole = i
        for _ in range(N):  # simulate N steps
            outhole = the_mapping[in_hole]
            next_in_hole = the_next_on_right[outhole]
            if next_in_hole == -1:
                break
            if next_in_hole == i:
                return 1
            in_hole = next_in_hole
    return 0


for mapping in mappings:
    #print(mapping, next_on_right, detect_cycle(mapping, next_on_right))
    answer += detect_cycle(mapping, next_on_right)


print(answer)
