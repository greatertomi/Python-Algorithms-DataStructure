# Print all possible permutations of a string
def permutations(string):
    if len(string) <= 1:
        return [string]
    elif len(string) == 2:
        return [string[0:], string[::-1]]
    else:
        output = []
        current_level = string[0]
        prev_level = permutations(string[1:])

        for element in prev_level:
            for pos in range(len(element) + 1):
                temp_string = ''
                temp_element = element
                pick_counter = -1
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_string += current_level
                    else:
                        temp_string += temp_element[pick_counter]
                        pick_counter -= 1

                output.append(temp_string)
        return output

# print(permutations('abcd'))

# Test Cases
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)
