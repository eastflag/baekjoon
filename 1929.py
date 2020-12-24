# 퍼포먼스 고려
# 1: n의 제곱근까지 계산
import math

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

start, end = map(int, input().split(' '))
for i in range(start, end + 1):
    if isPrime(i):
        print(i)

# 2: 아리스토체네스 방법 이용



