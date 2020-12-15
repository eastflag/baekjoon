enter = input()
# 대문자로 변경, 문자열을 루프돌면서 문자별 카운트하는 딕셔너리 생성, value중 최대값 구함. 최대값을 가진 문자와 갯수를 구함.
enter = enter.upper()
data = {}
for i in range(len(enter)):
    if enter[i] in data:
        data[enter[i]] += 1
    else:
        data[enter[i]] = 1
# print(data)
data_max = max(data.values())
character = ''
count = 0
for key in data.keys():
    if data[key] == data_max:
        character = key
        count += 1
if count > 1:
    print('?')
else:
    print(character)