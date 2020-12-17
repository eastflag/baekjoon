i = int(input())
x = i // 5
sum_xy = -1
for n in range(x, -1, -1):
    if (i - 5 * n) % 3 == 0:
        y = (i - 5 * n) // 3
        sum_xy = n + y
        break
print(sum_xy)
