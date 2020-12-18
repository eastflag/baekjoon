# 중앙값을 찾은 다음에 퀵소트한다.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def quick_conph(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]

    return quick_conph(left) + [pivot] + quick_conph(right)

count = int(input())
data = []
for i in range(count):
    data.append(int(input()))


data_sorted = quick_conph(data)
for n in data_sorted:
    print(n)

