def decode(string):
    current_char_multiplier = 0
    result = ''
    for char in string:
        if char.isdigit():
            current_char_multiplier = int(str(current_char_multiplier) + char)
        else:
            result = result + current_char_multiplier*char if current_char_multiplier > 0 else result + char
            current_char_multiplier = 0
    return result


def encode(string):
    current_char_count = 0
    current_char = ''
    result = ''
    for char in string:
        if char == current_char:
            current_char_count += 1
            if string.index(char) == len(string)-1:
                result = conduct_final_encoding(result, current_char_count, current_char)
        else:
            if current_char_count > 0:
                result = conduct_final_encoding(result, current_char_count, current_char)
            current_char = char
            current_char_count = 1
    result = conduct_final_encoding(result, current_char_count, current_char)
    return result


def conduct_final_encoding(current_result_string, char_count, current_char):

    return current_result_string + str(char_count) + current_char\
        if char_count > 1 else current_result_string + current_char
