t = int(input())
for _ in range(t):
    a, b = input().split()
    # Swap first characters
    new_a = b[0] + a[1:]
    new_b = a[0] + b[1:]
    print(new_a, new_b)