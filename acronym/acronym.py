import re


def abbreviate(words):
    words_without_punctuation = re.sub('-|_', ' ', words)
    splitted_words = words_without_punctuation.split()

    first_words_char = ''
    for splitted_word in splitted_words:
        first_words_char += splitted_word[0]

    return first_words_char.upper()
