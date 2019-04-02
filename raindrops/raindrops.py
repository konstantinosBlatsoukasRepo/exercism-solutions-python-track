FACTOR_THREE = 'Pling'
FACTOR_FIVE = 'Plang'
FACTOR_SEVEN = 'Plong'


def raindrops(number):
    pls = ''

    for factor in range(1, number + 1):
        if is_factor(3, factor, number):
            pls += FACTOR_THREE
        elif is_factor(5, factor, number):
            pls += FACTOR_FIVE
        elif is_factor(7, factor, number):
            pls += FACTOR_SEVEN

    if pls != '':
        return pls
    return str(number)


def is_factor(magic, factor, number):
    return factor == magic and number % factor == 0
