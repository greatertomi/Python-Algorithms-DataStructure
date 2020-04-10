def longest_consecutive_subsequence(input_list):
    numbers_set = set()
    return_dict = {}
    for i in input_list:
        numbers_set.add(i)

    num_array = set()
    counter = 1

    for element in numbers_set:
        if element + 1 in numbers_set:
            num_array.add(element)
            num_array.add(element + 1)
            # print(num_array)
        else:
            return_dict[counter] = num_array
            counter += 1
            num_array = set()

    # Returns the value of the dict that has the longest value
    # print(return_dict)
    max_length = len(return_dict[1])
    max_dict = 1
    for nums in return_dict:
        if len(return_dict[nums]) > max_length:
            max_length = len(return_dict[nums])
            max_dict = nums
    return_list = list(return_dict[max_dict])
    return return_list


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6], [8, 9, 10, 11, 12]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)


# print(longest_consecutive_subsequence([2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6]))
