def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, count_left = merge_sort_count(arr[:mid])
    right, count_right = merge_sort_count(arr[mid:])
    merged = []
    i = 0
    count = count_right + count_left
    for j in range(len(right)):
        while i < len(left) and left[i] <= 2 * right[j]:
            i += 1
        count += len(left) - i
    
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, count

n = int(input())
arr = list(map(int, input().split()))
_, count = merge_sort_count(arr)
print(count)