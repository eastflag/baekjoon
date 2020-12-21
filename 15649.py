from itertools import permutations

N, M = map(int, input().split(' '))

result = permutations(range(1, N + 1), M)
for i in list(result):
    print(" ".join(map(str, i)))