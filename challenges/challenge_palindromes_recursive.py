def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if len(word) == 1:
        return True

    if len(word) == 2 and word[0] == word[1]:
        return True

    if word[low_index] == word[high_index]:
        sliced_word = word[1:-1]
        new_higher_index = len(sliced_word) - 1
        return is_palindrome_recursive(sliced_word, 0, new_higher_index)
    else:
        return False
