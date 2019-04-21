import re


def word_count(phrase):
    lower_phrase = phrase.lower()
    splitted_words = __split_with_special_chars(lower_phrase)

    words_frequency = {}
    for current_word in splitted_words:
        if current_word in words_frequency:
            words_frequency[current_word] += 1
        else:
            words_frequency[current_word] = 1

    if '' in words_frequency:
        del words_frequency['']

    return words_frequency


def __split_with_special_chars(phrase):
    return re.split('[.?\-", _!& @$% ^:]|\s', phrase)
