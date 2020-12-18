# 팩토리얼 d(n) = n * d(n-1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

enter = int(input())
print(factorial(enter))