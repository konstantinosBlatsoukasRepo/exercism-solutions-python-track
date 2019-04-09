VALUE_ONE_LETTERS = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
VALUE_TWO_LETTERS = ['D', 'G']
VALUE_THREE_LETTERS = ['B', 'C', 'M', 'P']
VALUE_FOUR_LETTERS = ['F', 'H', 'V', 'W', 'Y']
VALUE_FIVE_LETTERS = ['K']

INCREMENTAL_VALUES_LETTERS = [VALUE_ONE_LETTERS, VALUE_TWO_LETTERS,
                              VALUE_THREE_LETTERS, VALUE_FOUR_LETTERS, VALUE_FIVE_LETTERS]

VALUE_EIGHT_LETTERS = ['J', 'X']
VALUE_TEN_LETTERS = ['Q', 'Z']


def score(word):
    letter_values = __initialize_letter_values()
    uppercased = word.upper()

    if word == "":
        return 0
    else:
        return calculate_score(uppercased, letter_values)


def __initialize_letter_values():
    letter_values = {}

    current_value = 1
    for letters in INCREMENTAL_VALUES_LETTERS:
        __insert_values(letters, letter_values, current_value)
        current_value += 1

    current_value = 8
    for letters in [VALUE_EIGHT_LETTERS, VALUE_TEN_LETTERS]:
        __insert_values(letters, letter_values, current_value)
        current_value += 2

    return letter_values


def __insert_values(letters, letter_values, value):
    for letter in letters:
        letter_values[letter] = value


def calculate_score(word, letter_values):
    return sum([letter_values[letter] for letter in word])


print(score("zoo"))
