import re

def verify(isbn):
    result = 0
    multiplier = 10
    isbn_digits = isbn.replace("-","")
    pattern = re.compile('\d{9}(\d|X)')
    if pattern.match(isbn_digits) and len(isbn_digits) == 10:
        for i in range(0, 9):
            result += int(isbn_digits[i])*multiplier
            multiplier -= 1
        if isbn_digits[9] == "X":
            result += 10
        else:
            result += int(isbn_digits[9])
        return result%11 == 0
    else:
        return False
