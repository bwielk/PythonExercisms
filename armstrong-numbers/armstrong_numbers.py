def is_armstrong(number):
    number_str = str(number)
    length_of_digits_in_number = len(number_str)
    result = 0
    for i in range(0, length_of_digits_in_number):
        result += int(number_str[i]) ** length_of_digits_in_number
    return result == number
