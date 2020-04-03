word = 'watering'


# Function to reverse a string
def string_reverser(string):
    new_string = ''
    neg_length = -len(string) - 1
    for i in range(-1, neg_length, -1):
        new_string += string[i]
    return new_string


# string reverser test cases
print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")
print('-----------------------------------------------------------')


# A function that checks if two strings are anagrams
# My solution
def anagram_checker(string1, string2):
    string1 = string1.lower().replace(' ', '')
    string2 = string2.lower().replace(' ', '')
    if len(string1) != len(string2):
        return False
    else:
        checker = False
        for i in range(len(string1)):
            index = string2.find(string1[0])
            if index != -1:
                string2 = string2[:index] + string2[index + 1:]
                string1 = string1[1:]
                checker = True
            else:
                checker = False
                break
        return checker


# Udacity's Solution
def anagram_checker2(str1, str2):
    if len(str1) != len(str2):
        # Clean strings
        clean_str_1 = str1.replace(" ", "").lower()
        clean_str_2 = str2.replace(" ", "").lower()

        if sorted(clean_str_1) == sorted(clean_str_2):
            return True
    return False

# Anagram checker test cases
print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
print('-----------------------------------------------')

# A function that takes a sentence and reverse each words
def word_flipper(sentence):
    sentence_list = sentence.split(' ')
    reversed_list = []
    for i in sentence_list:
        reversed_list.append(string_reverser(i))

    return ' '.join(reversed_list)


# Word flipper test cases
print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
print('-----------------------------------------------')

# A function that finds the hamming distance between two strings
def hamming_distance(string1, string2):
    if len(string1) != len(string2):
        return None
    else:
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                count += 1
        return count


# print(hamming_distance('cats', 'rats'))

# Hamming distance test cases
print("Pass" if (10 == hamming_distance('ACTTGACCGGG', 'GATCCGGTACA')) else "Fail")
print("Pass" if (1 == hamming_distance('shove', 'stove')) else "Fail")
print("Pass" if (None is hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print("Pass" if (9 == hamming_distance('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if (2 == hamming_distance('0101010100011101', '0101010100010001')) else "Fail")
