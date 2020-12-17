enter = int(input())
list = [enter]
while True:
    new = list[-1]
    new_c = list[-1]
    if new_c < 10:
        new_c *= 10
    new_c = new % 10 * 10 + (new_c // 10 + new_c % 10) % 10
    if list.count(new_c) > 0:
        break
    list.append(new_c)
print(len(list))