# , and a
PRESENTS = ['Partridge in a Pear Tree.', 'two Turtle Doves', 'three French Hens', 'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying',
            'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']

DAYS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
FIRST_SENTENCE = 'On the {} day of Christmas my true love gave to me: '


def recite(start_verse, end_verse):
    if start_verse == end_verse:
        return [build_recite(end_verse - 1)]
    else:
        return [build_recite(verse - 1) for verse in range(start_verse, end_verse + 1)]


def build_recite(index_verse):
    lyrics = FIRST_SENTENCE.format(DAYS[index_verse])

    if index_verse == 0:
        return lyrics + 'a ' + PRESENTS[index_verse]

    for index in range(index_verse, -1, -1):
        if index == 0:
            lyrics += 'and a ' + PRESENTS[index]
        else:
            lyrics += PRESENTS[index] + ', '
    return lyrics


print(recite(3, 3))
