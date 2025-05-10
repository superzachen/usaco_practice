n = int(input())
weights = list(map(int, input().split()))
def find_min_diff(i, sum1, sum2):
    if i == n:
        return abs(sum1 - sum2)
            
    diff1 = find_min_diff(i + 1, sum1 + weights[i], sum2)
    diff2 = find_min_diff(i + 1, sum1, sum2 + weights[i])
        
    return min(diff1, diff2)
    
result = find_min_diff(0, 0, 0)
print(result)