def raindrops(number):
    mapped_results =    {3: "Pling",
                        5: "Plang",
                        7: "Plong"}

    factors_of_a_number = []
    factor_exists = False

    for i in range(1, number+1):
        if number%i == 0:
            factors_of_a_number.append(i)

    result = ""
    for element in mapped_results.keys():
        if element in factors_of_a_number:
            result += mapped_results[element]
            factor_exists = True

    if factor_exists:
        return result
    else:
        return str(number)
