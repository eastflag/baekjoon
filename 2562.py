list = []
for n in range(9):
    list.append(int(input()))
maxNum = max(list)
print(maxNum)
print(list.index(maxNum) + 1)