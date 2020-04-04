def factorial(n):
    if n <= 1:
        return 1
    total = n * factorial(n - 1)
    return total


# print(factorial(0))

print("Pass" if (1 == factorial(0)) else "Fail")
print("Pass" if (1 == factorial(1)) else "Fail")
print("Pass" if (120 == factorial(5)) else "Fail")
