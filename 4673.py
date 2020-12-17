def eachsum(a):
    a_list_sum = a
    for n in list(str(a)):
        a_list_sum += int(n)
    return a_list_sum

input_list = []
for i in range(1, 10000 + 1):
    input_list.append(i)
for i in range(1, 10000 + 1):
    c = eachsum(i)
    if input_list.count(c) > 0:
        input_list.remove(c)
for n in input_list:
    print(n)

