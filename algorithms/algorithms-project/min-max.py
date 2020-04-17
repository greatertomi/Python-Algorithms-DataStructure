import random

def get_min_max(input_list):
    min_num = input_list[0]
    max_num = input_list[0]
    for i in input_list:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i

    return min_num, max_num

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# test = [4, 6, 3, 8, 5, 12, 1, 7]
# print(min_max(test))
