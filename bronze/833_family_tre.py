#https://usaco.org/index.php?page=viewproblem2&cpid=833
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
    return list(map(int, sys.stdin.readline().split()))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()


# -- End of Helpers --
m = []
d = []

lines, cowx, cowy = read_strs()
lines = int(lines)
out = ""

for _ in range(lines):
    mom, dot = read_strs()
    m.append(mom)
    d.append(dot)

xAnc = []
yAnc = []
cx = cowx
cy = cowy

while cx in d:
    xAnc.append(cx)
    tempX = d.index(cx)
    cx = m[tempX]
xAnc.append(cx)

while cy in d:
    yAnc.append(cy)
    tempY = d.index(cy)
    cy = m[tempY]
yAnc.append(cy)

common = ""
found = False
for x in xAnc:
    if found:
        break
    else:
        for y in yAnc:
            if x == y:
                common = x
                found = True
                break

if common == "":
    print("NOT RELATED")
else:
    xLvl = xAnc.index(common)
    yLvl = yAnc.index(common)

    if xLvl == yLvl and yLvl == 1:
        print("SIBLINGS")
    elif xLvl == yLvl or (xLvl > 1 and yLvl > 1):
        print("COUSINS")
    elif xLvl > yLvl:
        diff = xLvl - yLvl
        if cowy == common:
            if diff == 1:
                out = "mother"
            else:
                out = "great-" * (diff - 2) + "grand-mother"
            print(f"{cowy} is the {out} of {cowx}")
        else:
            if diff == 1:
                out = "aunt"
            else:
                out = "great-" * (diff - 1) + "aunt"
            print(f"{cowy} is the {out} of {cowx}")
    else:
        diff = yLvl - xLvl
        if cowx == common:
            if diff == 1:
                out = "mother"
            else:
                out = "great-" * (diff - 2) + "grand-mother"
            print(f"{cowx} is the {out} of {cowy}")
        else:
            if diff == 1:
                out = "aunt"
            else:
                out = "great-" * (diff - 1) + "aunt"
            print(f"{cowx} is the {out} of {cowy}")