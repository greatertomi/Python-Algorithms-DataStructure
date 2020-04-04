def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        check_times = int(len(string) / 2)
        if check_times == 0:
            return
        if string[0] == string[-1]:
            is_palindrome(string[1:-1])
            return True
        else:
            return False

print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")
