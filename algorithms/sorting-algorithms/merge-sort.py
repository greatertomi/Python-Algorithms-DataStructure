def merge(arr1, arr2):
    results = list()
    left_index = 0
    right_index = 0

    while left_index < len(arr1) and right_index < len(arr2):
        if arr2[right_index] > arr1[left_index]:
            results.append(arr1[left_index])
            left_index += 1
        else:
            results.append(arr2[right_index])
            right_index += 1

    while left_index < len(arr1):
        results.append(arr1[left_index])
        left_index += 1

    while right_index < len(arr2):
        results.append(arr2[right_index])
        right_index += 1

    return results

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

print(merge_sort([10, 24, 56, 38, 1, 42, 19]))
