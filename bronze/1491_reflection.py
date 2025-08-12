#https://usaco.org/index.php?page=viewproblem2&cpid=1491
# -- Helpers --
import sys
import os

problem_name = "gymnastics"

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
def main():
    n, q = read_ints()
    grid = [read_str() for _ in range(n)]
    smaller_grid = [[0] * (n // 2) for _ in range(n // 2)]
    ans = 0

    def update(x, y, scale):
        nonlocal ans
        if grid[x][y] == '.':
            return
        x = min(x, n - 1 - x)
        y = min(y, n - 1 - y)
        ans -= min(smaller_grid[x][y], 4 - smaller_grid[x][y])
        smaller_grid[x][y] += scale
        ans += min(smaller_grid[x][y], 4 - smaller_grid[x][y])

    for i in range(n):
        for j in range(n):
            update(i, j, 1)

    print(ans)
    for _ in range(q):
        x, y = read_ints()
        x -= 1
        y -= 1
        update(x, y, -1)
        grid[x] = grid[x][:y] + ('.' if grid[x][y] == '#' else '#') + grid[x][y + 1:]
        update(x, y, 1)
        print(ans)

if __name__ == "__main__":
    main()