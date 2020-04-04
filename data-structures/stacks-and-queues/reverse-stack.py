def reverse_stack(input_list):
    new_list = []
    for i in range(-1, -len(input_list)-1, -1):
        new_list.append(input_list[i])
    return new_list

print(reverse_stack([1, 2, 3, 4, -3]))
