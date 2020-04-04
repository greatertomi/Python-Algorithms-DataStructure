# Prints all possible permutation of a list
def permute(input_list):
    if len(input_list) <= 1:
        return [input_list]
    elif len(input_list) == 2:
        return [input_list, input_list[::-1]]
    else:
        output = []
        current_level = input_list[0]
        prev_level = permute(input_list[1:])

        for element in prev_level:
            for pos in range(len(element) + 1):
                temp_list = []
                temp_element = element.copy()
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list.append(current_level)
                    else:
                        temp_list.append(temp_element.pop())
                output.append(temp_list)
        return output

print(permute([1, 2, 3]))
