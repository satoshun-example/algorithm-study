from itertools import permutations


def lexicographic_permutations(value):
    perm =  permutations(value)
    for i in range(999999):
        next(perm)

    return ''.join(next(perm))



print(lexicographic_permutations('0123456789'))
