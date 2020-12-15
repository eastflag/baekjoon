# 문자에 해당하는 숫자를 찾고, 숫자+1의 합계를 구한다.
enter = input()
A = list(enter)
A_num = []
data = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
for n in A:
    for key in data.keys():
        if key.find(n) >= 0:
            A_num.append(data[key])
            break
# print(A_num)
print(sum(A_num) + len(A_num))