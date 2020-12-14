count = int(input())
for n in range(count):
    i = input().split(' ')
    nums = []
    for m in range(1, len(i)):
        if m != 0:
            nums.append(int(i[m]))
    # print(nums)
    avg = sum(nums) / len(nums)
    # print(avg)
    num = 0
    for k in nums:
        if k > avg:
            num += 1
    # print(num)
    print(format(round(num / len(nums) * 100, 3), '.3f') + '%')
