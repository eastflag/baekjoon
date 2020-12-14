import sys

i = sys.stdin.readline().rstrip()
for n in range(0, int(i)):
    i = sys.stdin.readline().rstrip().split(' ')
    A = int(i[0])
    B = int(i[1])
    print(A + B)