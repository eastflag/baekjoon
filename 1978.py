# 소수찾기 n이 있으면 루트n까지 루프를 돌리는것이 가장 최적 알고리즘
count =int(input())
data = list(map(int, input().split(' ')))

def sosu(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0
for n in data:
    if sosu(n):
        sum += 1
print(sum)