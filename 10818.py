i = input()
N = int(i)
i = input().split(' ')
list = []
for n in range(len(i)):
    list.append(int(i[n]))
# max = list[0]
# min = list[0]
# for n in list:
#     if max < n:
#         max = n
#     if min > n:
#         min = n
# print(min, end=" ")
# print(max)
print(min(list), end=" ")
print(max(list))