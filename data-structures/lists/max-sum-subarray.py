nums = [1, 2, -5, -4, 1, 6]

def sum_list(input_list: list) -> int:
    result = 0
    for i in input_list:
        result += i
    return result

def sublist_generator(input_list: list) -> list:
    list_of_lists = []
    list_max_pos = len(input_list) + 1

    for inital_sublist_pos in range(list_max_pos):
        for final_sublist_pos in range(inital_sublist_pos+1, list_max_pos):
            list_of_lists.append(input_list[inital_sublist_pos:final_sublist_pos])
    return list_of_lists

def max_sum_subarray(input_list: list):
    max_val = -float("inf")
    list_of_lists = sublist_generator(input_list)
    for list in list_of_lists:
        list_added = sum_list(list)
        if list_added > max_val:
            max_val = list_added

    return max_val

# print(sublist_generator(nums))
# print(max_sum_subarray(nums))

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1, 2, 3, -4, 6]
solution = 8 # sum of array
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements
test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]
test_case = [arr, solution]
test_function(test_case)

