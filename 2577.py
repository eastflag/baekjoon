result = 1
for n in range(3):
    result *= int(input())
result = str(result)

number_list = []
for n in range(10):
    number_list.append(0)

for n in range(len(result)):
    number_list[int(result[n])] += 1

for n in number_list:
    print(n)
