def on_square(integer_number):
    range_exception_raiser(integer_number)
    grains_in_previous_square = 1
    for current_square in range(2, integer_number+1):
        grains_in_previous_square = grains_in_previous_square*2
    return grains_in_previous_square

def total_after(integer_number):
    range_exception_raiser(integer_number)
    result = 1
    grains_in_previous_square = 1
    for current_square in range(2, integer_number + 1):
        grains_in_previous_square = grains_in_previous_square * 2
        result += grains_in_previous_square
    return result

def range_exception_raiser(integer_number):
    if integer_number < 1 or integer_number > 64:
        raise ValueError('The argument value must be higher than 0 and less that 65')