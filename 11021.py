i = input()
for n in range(1, int(i) + 1):
    i = input().split(' ')
    sum = int(i[0]) + int(i[1])
    print('Case #%d: %d' % (n, sum))