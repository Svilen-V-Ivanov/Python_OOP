from itertools import permutations


def possible_permutations(sequence):
    for value in permutations(sequence):
        yield list(value)


[print(n) for n in possible_permutations([1, 2, 3])]
