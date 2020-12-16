# y = A + (B-C)x 의 일차 방정식의 해를 구한다.
# 만일 기울기가 음수이거나 0이면 해가 없다.
enter = input().split(' ')
A = int(enter[0])
B = int(enter[1])
C = int(enter[2])
if (B - C) >= 0:
    print(-1)
else:
    for i in range(2100000000):
        # if (A + B * i) < C * i:
        if A < (C - B) * i:
            print(i)
            break
