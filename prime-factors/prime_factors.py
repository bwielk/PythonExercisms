def prime_factors(natural_number):
    number = natural_number
    result = []
    primes_in_range = list(filter(lambda x: is_prime(x), range(2, natural_number+1)))
    loop_goes_on = True
    while loop_goes_on:
        loop_goes_on = False
        for i in primes_in_range:
            if number % i == 0:
                result.append(i)
                number = number // i
                loop_goes_on = True
    return sorted(result)


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
