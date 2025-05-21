# https://codeforces.com/contest/1216/problem/C
# -- Helpers --
import sys
import os

problem_name = "billboard"

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
x1, y1, x2, y2 = read_ints()
x3, y3, x4, y4 = read_ints()
x5, y5, x6, y6 = read_ints()


def point_in_rectangle(px, py, x1, y1, x2, y2):
    return x1 <= px <= x2 and y1 <= py <= y2


def rectangle_in_rectangle(sx1, sy1, sx2, sy2, bx1, by1, bx2, by2):
    return point_in_rectangle(sx1, sy1, bx1, by1, bx2, by2) and point_in_rectangle(
        sx2, sy2, bx1, by1, bx2, by2
    )


def overlaping(x1, y1, x2, y2, x3, y3, x4, y4):
    return (
        point_in_rectangle(x1, y1, x3, y3, x4, y4)
        or point_in_rectangle(x2, y2, x3, y3, x4, y4)
        or point_in_rectangle(x2, y1, x3, y3, x4, y4)
        or point_in_rectangle(x1, y2, x3, y3, x4, y4)
        or point_in_rectangle(x3, y3, x1, y1, x2, y2)
        or point_in_rectangle(x4, y4, x1, y1, x2, y2)
        or point_in_rectangle(x3, y4, x1, y1, x2, y2)
        or point_in_rectangle(x4, y3, x1, y1, x2, y2)
    )


covered = False

if rectangle_in_rectangle(x1, y1, x2, y2, x3, y3, x4, y4) or rectangle_in_rectangle(
    x1, y1, x2, y2, x5, y5, x6, y6
):
    covered = True
else:
    if overlaping(x3, y3, x4, y4, x5, y5, x6, y6):
        bl_covered = point_in_rectangle(x1, y1, x3, y3, x4, y4) or point_in_rectangle(
            x1, y1, x5, y5, x6, y6
        )
        tl_covered = point_in_rectangle(x1, y2, x3, y3, x4, y4) or point_in_rectangle(
            x1, y2, x5, y5, x6, y6
        )
        br_covered = point_in_rectangle(x2, y1, x3, y3, x4, y4) or point_in_rectangle(
            x2, y1, x5, y5, x6, y6
        )
        tr_covered = point_in_rectangle(x2, y2, x3, y3, x4, y4) or point_in_rectangle(
            x2, y2, x5, y5, x6, y6
        )
        if bl_covered and tl_covered and br_covered and tr_covered:
            covered = True

print("NO" if covered else "YES")
