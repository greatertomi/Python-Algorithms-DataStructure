def sort_reversed(input_list):
    new_list = list()
    for i in range(len(input_list)):
        max_num = max(input_list)
        new_list.append(max_num)
        input_list.remove(max_num)

    return new_list

def rearrange_digits(input_list):
    input_list = sort_reversed(input_list)
    number1 = ''
    number2 = ''

    for i in range(len(input_list)):
        if i % 2 == 0:
            number1 += str(input_list[i])
        else:
            number2 += str(input_list[i])

    return [int(number1), int(number2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
#
array = [4, 6, 2, 5, 9, 8]
print(rearrange_digits(array))

test = [4, 6, 3, 8, 5, 12, 1, 7]
print(sort_reversed(test))
