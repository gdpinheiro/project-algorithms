def sort_strings(word):
    word_len = len(word)

    for index in range(word_len):
        for item in range(word_len - index - 1):
            if word[item] > word[item + 1]:
                current_element = word[item]
                word[item] = word[item + 1]
                word[item + 1] = current_element

    return word


def is_anagram(first_string, second_string):
    lower_first_string = list(first_string.lower())
    lower_second_string = list(second_string.lower())

    sorted_first_string = sort_strings(lower_first_string)
    sorted_second_string = sort_strings(lower_second_string)

    return sorted_first_string == sorted_second_string
