def classify(number):
    if number <= 0:
        raise ValueError('The method accepts integers larger than 0 only')
    results = []
    for i in range(1, number):
        if number%i == 0:
            results.append(i)
    sum_of_results = sum(results)
    if number == sum_of_results:
        return 'perfect'
    elif sum_of_results > number:
        return 'abundant'
    else:
        return 'deficient'
