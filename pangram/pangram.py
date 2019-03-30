import re

TOTAL_ALPHABET_LETTERS = 26


def is_pangram(sentence):
    if sentence == '':
        return False
    else:
        splitted = re.split(' |_|"|\.|\d', sentence)
        sentence_letters = ''.join(splitted)
        low_case_sentence = sentence_letters.lower()
        total_uniqueue_chars = len(set(low_case_sentence))

        return TOTAL_ALPHABET_LETTERS == total_uniqueue_chars
