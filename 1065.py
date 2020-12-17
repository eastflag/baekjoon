enter = int(input())
a_list = []
for i in range(1, enter + 1):
    if i < 100:
        a_list.append(i)
    else:
        i_list = list(str(i))
        if len(i_list) == 3:
            if int(i_list[2]) - int(i_list[1]) == int(i_list[1]) - int(i_list[0]):
                a_list.append(i)
print(len(a_list))