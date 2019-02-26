def say(number):
    validate_the_argument(int(number))
    number_to_translate = int(number)
    result = ''
    if number_to_translate == 0:
        return 'zero'
    large_units = [(1000000000, ' billion '), (1000000, ' million '), (1000, ' thousand ')]
    for unit in large_units:
        if number_to_translate // unit[0] > 0:
            num_of_billions = number_to_translate // unit[0]
            result += convert_0_999(num_of_billions) + unit[1]
            number_to_translate -= unit[0] * num_of_billions
            result += 'and ' if number_to_translate > 0 and number_to_translate < 100 else ''
    result += convert_0_999(number_to_translate)
    return result.strip()


def convert_0_999(number_to_translate):
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
             'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    result = ''
    if number_to_translate//100 > 0:
        result += units[number_to_translate//100] + ' hundred'
        number_to_translate -= 100*(number_to_translate//100)
        if number_to_translate > 0:
            result += ' and '
    if number_to_translate//10 >= 2:
        result += tens[number_to_translate//10]
        number_to_translate -= 10*(number_to_translate//10)
        if number_to_translate > 0 and number_to_translate < 10:
            result += '-'
    if number_to_translate//10 == 1:
        result += teens[number_to_translate-10]
        number_to_translate -= 10
        return result
    if number_to_translate//10 == 0:
        result += units[number_to_translate-10]
    return result


def validate_the_argument(number):
    if number < 0 or number > 1000000000000-1:
        raise ValueError('The number is too large or too small: please enter a number'
                         'between 0 and 999 999 999 999')