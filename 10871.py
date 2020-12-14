i = input().split(' ')
N = int(i[0])
X = int(i[1])
i = input().split(' ')

for n in range(len(i)):
    if X > int(i[n]):
        print(i[n], end=" ")