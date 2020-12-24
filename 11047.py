count, K = map(int, input().split(' '))
data = []
for i in range(count):
    data.append(int(input()))
data.sort(reverse=True)

sum = 0
for d in data:
    n = K // d
    sum += n
    if K % d == 0:
        break
    else:
        K = K - d * n

print(sum)