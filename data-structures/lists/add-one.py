value = [9, 9, 9]

def add_one(input_list) -> list:
    num = ''
    new_list = []
    for i in input_list:
        num += str(i)
    new_num = int(num) + 1
    new_list = [int(i) for i in str(new_num)]
    return new_list

# Test Function
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

# Test case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test case 3
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# print(add_one(value))
