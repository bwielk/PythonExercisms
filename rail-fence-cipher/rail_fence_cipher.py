def encode(message, rails):
    result = ''
    if rails == 2:
        result += message[::rails]
        result += message[1::rails]
    elif rails == 3:
        result += message[::rails+1]
        rails -= 1
        result += message[1::rails]
        rails += 2
        result += message[2::rails]
    elif rails == 4:
        result += message[::6]
        second_row_factor = 1
        index = 1
        for i in range(0, len(message)):
            if index <= len(message):
                result += message[index]
                second_row_factor = 4 if second_row_factor <= 2 else 2
                index += second_row_factor
            else:
                break
        second_row_factor = 0
        index = 2
        for i in range(0, len(message)):
            if index <= len(message):
                result += message[index]
                second_row_factor = 2 if second_row_factor < 4 else 4
                index += second_row_factor
            else:
                break


    return result

def decode(encoded_message, rails):
    pass
