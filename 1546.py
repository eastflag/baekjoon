count = int(input())
i = input().split(' ')
nums = []
for n in range(count):
    nums.append(int(i[n]))
m = max(nums)
for n in range(count):
    nums[n] = nums[n] / m * 100
print(sum(nums) / len(nums))
