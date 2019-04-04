import re


def is_isogram(string):
    new_string = remove_whites_and_hyphens(string)
    lower_string = new_string.lower()

    total_chars = len(lower_string)
    total_unique_chars = len(set(lower_string))

    return total_chars == total_unique_chars


def remove_whites_and_hyphens(string):
    return re.sub("\s|-", "", string)
