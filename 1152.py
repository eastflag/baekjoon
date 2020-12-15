enter = input().strip()
# 단어는 없고 공백만 들어오는 경우가 있다.
if enter == '':
    print(0)
else:
    print(len(enter.split(' ')))