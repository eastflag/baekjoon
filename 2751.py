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

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)
    # BUILD-MAX-HEAP (A) : 위의 1단계
    # 인덱스 : (n을 2로 나눈 몫-1)~0
    # 최초 힙 구성시 배열의 중간부터 시작하면
    # 이진트리 성질에 의해 모든 요소값을
    # 서로 한번씩 비교할 수 있게 됨 : O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    # Recurrent (B) : 2~4단계
    # 한번 힙이 구성되면 개별 노드는
    # 최악의 경우에도 트리의 높이(logn)
    # 만큼의 자리 이동을 하게 됨
    # 이런 노드들이 n개 있으므로 : O(nlogn)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

# count = int(input())
# data = []
# for i in range(count):
#     data.append(int(input()))
#
#
# data_sorted = merge_sort(data)
# for n in data_sorted:
#     print(n)

import sys

n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')