def bubble_sort(input_list):
    noSwaps = None
    for i in range(len(input_list), 0, -1):
        for j in range(0, i-1):
            if input_list[j] > input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
                noSwaps = False
        if noSwaps:
            break
    return input_list


print(bubble_sort([43, 12, 88, 19, 14, -3]))
