import string

def rotate(text, key):
    if type(text) is str and type(key) is int:
        alphabet = list(string.ascii_lowercase)
        key = key - (key//len(alphabet))*len(alphabet) if key > len(alphabet) else key
        return conduct_rotation(key, text, alphabet)
    else:
        raise ValueError("Invalid arguments. The method accepts a string of text and an integer rotation key value")

def conduct_rotation(key, text, alphabet):
    result = ''
    found_char = None
    if key == 0:
        return text
    else:
        for i in range(0, len(text)):
            if text[i].isalpha():
                if alphabet.index(text[i].lower()) + key > len(alphabet) - 1:
                    index_of_desired_char = len(alphabet) - (alphabet.index(text[i].lower()) + key)
                    found_char = alphabet[
                        index_of_desired_char // -1 if index_of_desired_char < 0 else index_of_desired_char // 1]
                else:
                    found_char = alphabet[alphabet.index(text[i].lower()) + key]
                pass
                result += found_char.upper() if text[i].isupper() else found_char.lower()
            else:
                result += text[i]
    return result
