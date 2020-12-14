# case = input()
i = input().split(' ')
x1 = int(i[0])
y1 = int(i[1])
r1 = int(i[2])
x2 = int(i[3])
y2 = int(i[4])
r2 = int(i[5])
distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
sum = (r1 + r2) ** 2

if distance == 0:
    print(-1)
elif distance == sum:
    print(1)
elif distance < sum:
    print(2)
else:
    print(0)