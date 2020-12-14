i = input()
for n in range(1, int(i) + 1):
    i = input().split(' ')
    A = int(i[0])
    B = int(i[1])
    sum = A + B
    print('Case #%d: %d + %d = %d' % (n, A, B, A + B))