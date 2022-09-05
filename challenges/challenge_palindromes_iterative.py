def is_palindrome_iterative(word):
    split_word = []

    if word == "":
        return False

    for letter in word:
        split_word.append(letter)

    split_word.reverse()

    return word == "".join(split_word)
