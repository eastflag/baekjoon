enter = input().split(' ')
A = enter[0]
B = enter[1]

A_list = list(A)
B_list = list(B)
A_list.reverse()
B_list.reverse()
A_reverse = ''.join(A_list)
B_reverse = ''.join(B_list)
# print(A_reverse)
if A_reverse > B_reverse:
    print(A_reverse)
else:
    print(B_reverse)