def is_palindrome(word):
    word_list = list(word)
    for i in range(len(word_list)):
        if (word_list[i] == word_list[- 1]) or (word_list[i] == word_list[- i - 1]):
            continue
        else:
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))