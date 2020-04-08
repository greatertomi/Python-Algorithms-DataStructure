def subsets(arr):
    if len(arr) <= 1:
        return [arr]
    else:
        results = list()
        results.append([])
        results.append(arr)

        for i_pos in range(len(arr)):
            temp_arr = arr.copy()
            temp_arr.pop(i_pos)
            results.extend(subsets(temp_arr))

        results_mod = []
        for i, item in enumerate(results):
            if i == results.index(item):
                results_mod.append(item)
            else:
                pass
        return results_mod


print(subsets([1, 2, 3]))
