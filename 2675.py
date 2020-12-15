count = int(input())
for i in range(count):
    enter = input().split(' ')
    r = int(enter[0])
    str = enter[1]
    output = ''
    for j in range(len(str)):
        output += str[j] * r
    print(output)