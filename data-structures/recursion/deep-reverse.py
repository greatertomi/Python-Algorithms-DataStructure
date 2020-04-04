def deep_reverse(num_list):
    reversed_list = []
    for i in range(-1, -len(num_list) - 1, -1):
        if type(num_list[i]) == list:
            reversed_list.append(deep_reverse(num_list[i]))
        else:
            reversed_list.append(num_list[i])

    return reversed_list


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3], 4, [5, 6]]
solution = [[6, 5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

# print(deep_reverse(['3', '5', '7', ['6', '9', '10'], '-2']))
