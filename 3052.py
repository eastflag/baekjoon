nums = []
for n in range(10):
    nums.append(int(input()) % 42)

# print(nums)
# print(set(nums))
result = list(set(nums))
# print(result)
print(len(result))