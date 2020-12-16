# 현재 문자와 다음 문자가 같은지 비교하여 같으면 삭제한 문자열 생성
# 생성된 문자열과 중복을 제거한 문자열이 길이가 같은지 체크하여 같지 않으면 그룹문자

# a = 'aaabccabcc'
# a_list = []
# a_list_copy = list(a)
# for i in range(len(a_list_copy)):
#     if i == len(a_list_copy) - 1:
#         a_list.append(a_list_copy[i])
#     else:
#         if a_list_copy[i] != a_list_copy[i + 1]:
#             a_list.append(a_list_copy[i])
# print(a_list)

count = int(input())
sum = 0
for j in range(count):
    enter = input()
    enter_list = []
    enter_list_copy = list(enter)
    for i in range(len(enter_list_copy)):
        if i == len(enter_list_copy) - 1:
            enter_list.append(enter_list_copy[i])
        else:
            if enter_list_copy[i] != enter_list_copy[i + 1]:
                enter_list.append(enter_list_copy[i])

    enter_list_set = list(set(enter_list))
    if len(enter_list) == len(enter_list_set):
        sum += 1

print(sum)