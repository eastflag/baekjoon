# 피보나치 f(n) = f(n-1) + f(n-2)
def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

enter = int(input())
result = fibonachi(enter)
print(result)