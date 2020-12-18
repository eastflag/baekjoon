# nCr 경우의 수 구하기
count, M = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
# print(count, M, data)
answer = 0
for i in range(count):
    for j in range(i + 1, count):
        for k in range(j + 1, count):
            # print(data[i], data[j], data[k])\
            s = data[i] + data[j] + data[k]
            if s <= M:
                if answer < s:
                    answer = s
print(answer)