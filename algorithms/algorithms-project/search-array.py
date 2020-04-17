def rotated_array_search(input_list, number):
    start = 0
    end = len(input_list) - 1
    middle = (start + end) // 2
    while input_list[middle] != number and start <= end:
        if number < input_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2

    if input_list[middle] == number:
        return middle
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 3))

# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 10])
