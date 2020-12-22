def divide_sum(n):
    str_n = str(n)
    d_sum = n
    for i in range(len(str_n)):
        d_sum += int(str_n[i])
    return d_sum

enter = int(input())
answer = 0
for i in range(1, 1000000):
    result = divide_sum(i)
    # print(result)
    if result == enter:
        answer = i
        break
print(answer)