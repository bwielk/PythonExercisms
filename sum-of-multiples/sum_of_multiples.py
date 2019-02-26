def sum_of_multiples(limit, multiples):
    if type(multiples) is list and type(limit) is int and all(type(x) is int for x in multiples):
        list_of_natural_numbers_below_limit_with_multiples_in_multiples = []
        for multiple in list(set(multiples)):
            for i in range(limit-1, 0, -1):
                try:
                    if i % multiple == 0 and i not in list_of_natural_numbers_below_limit_with_multiples_in_multiples:
                        list_of_natural_numbers_below_limit_with_multiples_in_multiples.append(i)
                except ZeroDivisionError:
                    list_of_natural_numbers_below_limit_with_multiples_in_multiples.append(0)
        return sum(list_of_natural_numbers_below_limit_with_multiples_in_multiples)
    else:
        raise ValueError('Incorrect arguments.\
                        Argument "limit" should be an int and "multiples" should be a list of ints')
