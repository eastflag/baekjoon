i = input().split(' ')
A = int(i[0])
B = int(i[1])
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')