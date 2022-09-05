def is_palindrome_recursive(word, low_index, high_index):
    split_word = []

    if word == "":
        return False

    for letter in word:
        split_word.append(letter)

    split_word.reverse()

    return word == "".join(split_word)
