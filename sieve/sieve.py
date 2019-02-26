def sieve(limit):
    list_of_numbers_until_limit = list(range(2, limit+1))
    for i in range(0, len(list_of_numbers_until_limit)):
        try:
            current_num = list_of_numbers_until_limit[i]
            for x in range(i, len(list_of_numbers_until_limit)):
                if x+current_num <= len(list_of_numbers_until_limit):
                    if not is_prime(list_of_numbers_until_limit[x+current_num]):
                        list_of_numbers_until_limit.pop(x+current_num)
        except IndexError:
            continue
    return list_of_numbers_until_limit

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



