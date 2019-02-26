def numeral(number):
    result = []
    arabic_to_roman = {1: 'I'}
    number_to_process = number
    while number_to_process > 0:
        for arabic, roman in arabic_to_roman.items():
            if arabic <= number_to_process:
                result.append(arabic_to_roman[arabic])
                number_to_process -= arabic
    return ''.join(result)
