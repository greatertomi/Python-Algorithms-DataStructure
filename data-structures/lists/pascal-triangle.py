def factorial(num):
    if num <= 0:
        return 1
    fact = num * factorial(num - 1)
    return fact

def combination(top_num, bottom_num):
    bottom_analysis = factorial(top_num - bottom_num) * factorial(bottom_num)
    answer = factorial(top_num)/bottom_analysis
    return int(answer)

def nth_row_pascal(n):
    coefficient_list = []
    for i in range(n+1):
        coefficient_list.append(combination(n, i))

    return coefficient_list

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")

# Test Cases
n = 0
solution = [1]
test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]
test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]
test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]
test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]
test_case = [n, solution]
test_function(test_case)
