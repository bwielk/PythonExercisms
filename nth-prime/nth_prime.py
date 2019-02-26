def nth_prime(positive_number):
    if positive_number <= 0:
        raise ValueError('The value of the argument must be greater than 0')
    results = []
    num_of_found_primes = 0
    number_to_check = 2
    while num_of_found_primes < positive_number:
        if is_prime(number_to_check):
            results.append(number_to_check)
            num_of_found_primes += 1
        number_to_check += 1
    return results[positive_number-1]


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
