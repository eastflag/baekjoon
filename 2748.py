# f(n) = f(n-1) + f(n-2)
dic = {}

def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n - 1 not in dic:
            dic[n-1] = fibonachi(n-1)
        if n - 2 not in dic:
            dic[n-2] = fibonachi(n - 2)
        return dic.get(n - 1) + dic.get(n - 2)

n = int(input())
print(fibonachi(n))
