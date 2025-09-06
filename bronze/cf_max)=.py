t = int(input())
for _ in range(t):
    n = int(input())
    max_sum = -1
    best_x = -1
    for x in range(2, n + 1):
        k = n // x
        total = x * k * (k + 1) // 2
        if total > max_sum:
            max_sum = total
            best_x = x
    print(best_x)