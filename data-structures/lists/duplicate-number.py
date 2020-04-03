def duplicate_number(arr):
    num_freq_dict = {}
    duplicate = 0
    for i in arr:
        if i in num_freq_dict:
            num_freq_dict[i] += 1
        else:
            num_freq_dict[i] = 1
    for num, value in num_freq_dict.items():
        if value > 1:
            duplicate = num
    return duplicate

def duplicate_number2(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    for i in arr:
        if arr.count(i) == 2:
            return i
        else:
            pass

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5
test_case = [arr, solution]
test_function(test_case)

# nums = [0, 2, 3, 1, 4, 5, 3]
# print(duplicate_number(nums))
