import math

def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    middle = math.floor((start + end) / 2)

    while arr[middle] != num and start <= end:
        if num < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)

    if arr[middle] == num:
        return middle
    return -1

array = [1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19]
print(binary_search(array, 16))
