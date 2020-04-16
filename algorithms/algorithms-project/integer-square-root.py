# Partly correct
def square_root(num):
    if num < 0:
        return None
    elif num == 0 or num == 1:
        return num

    sqrt = 1
    counter = 2
    while counter <= num // 2:
        if num % (counter ** 2) == 0:
            num = num / (counter ** 2)
            sqrt *= counter
        else:
            counter += 1

    return sqrt

# Totally correct
def square_root2(number):
    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    i_start = 0
    i_end = number // 2
    result = None

    while i_start <= i_end:
        i_middle = (i_end + i_start) // 2
        i_middle_pow = i_middle * i_middle
        print(i_middle, i_middle_pow)

        if i_middle_pow == number:
            return i_middle
        elif i_middle_pow < number:
            i_start = i_middle + 1
            result = i_middle
        else:
            i_end = i_middle - 1

    return result

# print(square_root2(64))

print("Pass" if (3 == square_root(9)) else "Fail")
print("Pass" if (0 == square_root(0)) else "Fail")
print("Pass" if (4 == square_root(16)) else "Fail")
print("Pass" if (1 == square_root(1)) else "Fail")
print("Pass" if (5 == square_root(27)) else "Fail")
print("Pass" if (None is square_root(-1)) else "Fail")
print("Pass" if (99380 == square_root(9876543210)) else "Fail")
