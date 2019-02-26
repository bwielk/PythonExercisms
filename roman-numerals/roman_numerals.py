def numeral(number):
    result = []
    arabic_to_roman = {
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}
    number_to_process = number
    while number_to_process > 0:
        for arabic, roman in arabic_to_roman.items():
            if arabic <= number_to_process:
                amount_of_unit = number_to_process // arabic
                result.append(amount_of_unit*arabic_to_roman[arabic])
                number_to_process -= amount_of_unit*arabic
    return ''.join(result)
