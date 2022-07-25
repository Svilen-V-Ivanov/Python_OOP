def get_value(number):
    if number <= 1:
        return False

    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    return is_prime


def get_primes(sequence):
    for number in sequence:
        if get_value(number):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
