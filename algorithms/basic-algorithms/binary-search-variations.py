def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left + center)
    else:
        return recursive_binary_search(target, source[:center], left)

def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None

    new_index = -1
    while source[index-1] == source[index]:
        new_index = index - 1
        index -= 1
    if new_index != -1:
        return new_index
    else:
        return index

def contains(target, source):
    return recursive_binary_search(target, source) is not None
    # index = recursive_binary_search(target, source)
    # if index is not None:
    #     return True
    # else:
    #     return False

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters))
print(contains('b', letters))

# array = [1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19]
# array = [1, 3, 4, 7, 7, 7, 8, 11, 12]
# print(recursive_binary_search(7, array))
# print(find_first(10, array))
