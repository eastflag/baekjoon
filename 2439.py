i = input()
A = int(i)
for n in range(1, A + 1):
    print(' ' * (A - n) + '*' * n)