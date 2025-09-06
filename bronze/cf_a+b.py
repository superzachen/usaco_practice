t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Two-digit number
    digit_sum = n // 10 + n % 10  # Tens digit + Units digit
    print(digit_sum)