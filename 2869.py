#  등차 수열 C = (A) + (n - 1)(A - B)
import math
A, B, C = map(int, input().split(' '))
n = math.ceil((C - A) / (A - B) + 1)
print(n)
# for i in range(n, 0, -1):
#     height = A + (i - 1) * (A - B)
#     if height < C:
#         print(i+1)
#         break