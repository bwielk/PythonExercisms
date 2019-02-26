def square_of_sum(count):
    result = 0
    for i in range(0, count+1):
        result += i
    return result**2

def sum_of_squares(count):
    result = 0
    for i in range(0, count+1):
        result += i**2
    return result

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
