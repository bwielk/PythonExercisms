from functools import reduce

def largest_product(series, size):
    validate_attributes(series, size)
    if (series == '' and size == 0) or size == 0:
        return 1
    list_of_digits = list(map(lambda x: int(x), series))
    results = {}
    for i in range(0, len(series)):
        found_series_string = list_of_digits[i:i+size]
        found_series_string_product = reduce(lambda x, y: x*y, found_series_string)
        results["".join(str(v) for v in found_series_string)] = found_series_string_product
        if i+size == len(series):
            break
    #the method below finds the highest value in the dictionary
    return results.get(max(results, key=results.get))

def validate_attributes(series, size):
    if size > len(series) or (series == '' and size > 0) or any(x.isalpha() for x in series) or size < 0:
        raise ValueError('Wrong attributes. Series should not be an empty'
                         ' and should not be shorter than the size attribute')