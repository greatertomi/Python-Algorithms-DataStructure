def minimum_bracket_reversals(input_string):
    lenn = len(input_string)

    if lenn % 2:
        return -1

    stack = []
    for i in range(lenn):
        if input_string[i] == '' and len(stack):
            if stack[0] == '':
                stack.pop(0)
            else:
                stack.insert(0, input_string[i])
        else:
            stack.insert(0, input_string[i])

    red_len = len(stack)

    n = 0
    while len(stack) and stack[0] == '':
        stack.pop(0)
        n += 1

    return red_len // 2 + n % 2

# brackets = '{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}'
# print(minimum_bracket_reversals(brackets.strip()))

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")

test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)

test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_5)
