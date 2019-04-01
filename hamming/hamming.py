
def distance(strand_a, strand_b):
    strand_a_len = len(strand_a)
    strand_b_len = len(strand_b)

    if strand_a_len != strand_b_len:
        raise ValueError('strand lengths must be equal')
    else:
        return __calculate_hamming_distance(strand_a, strand_b)


def __calculate_hamming_distance(strand_a, strand_b):
    if __have_same_length(strand_a, strand_b):
        return 0
    else:

        distance = 0
        for index in range(0, len(strand_a)):
            if strand_a[index] != strand_b[index]:
                distance += 1

        return distance


def __have_same_length(strand_a, strand_b):
    return len(strand_a) == 0 and len(strand_a) == 0
