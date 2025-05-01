cap1, buk1 = map(int, input().split())
cap2, buk2 = map(int, input().split())
cap3, buk3 = map(int, input().split())

TURN_NUM = 100

for i in range(TURN_NUM + 1):
    if i%3 == 1:
        amount_changed = min(buk1, cap2-buk2)
        buk1 -= amount_changed
        buk2 += amount_changed
    if i%3 == 2:
        amount_changed = min(buk2, cap3-buk3)
        buk2 -= amount_changed
        buk3 += amount_changed
    if i%3 == 0:
        amount_changed = min(buk3, cap1-buk1)
        buk3 -= amount_changed
        buk1 += amount_changed


print(buk1)
print(buk2)
print(buk3)