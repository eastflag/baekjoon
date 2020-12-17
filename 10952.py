while True:
    enter = input().split(' ')
    A = int(enter[0])
    B = int(enter[1])
    if A == 0 and B == 0:
        break
    print(A + B)