# Sum of all integers from 1 to n
def sum_integers(n):
    if n == 1:
        return 1
    total = n + sum_integers(n - 1)
    return total
print(sum_integers(5))


