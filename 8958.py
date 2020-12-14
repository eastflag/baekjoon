count = int(input())
for n in range(count):
    num = input()
    count = 0
    sum = 0
    for i in range(len(num)):
        if num[i] == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)