def slices(series, length):
    series_result = []
    if length > len(series) or length < 1 or not all(digit.isdigit() for digit in series):
        raise ValueError(r".+")
    else:
        for i in range(0, len(series)):
            if i + length-1 < len(series):
                series_result.append(drop_zeros_in_the_beginning_of_a_number(series[i: i+length]))
    return series_result


def drop_zeros_in_the_beginning_of_a_number(number):
    number_to_process = number
    for i in range(0, len(number)):
        if number[i] == '0':
            number_to_process = number_to_process[1:]
        else:
            break
    return number_to_process
