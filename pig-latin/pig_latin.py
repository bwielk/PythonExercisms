def translate(text):
    vowels_and_consonants_treated_as_vowels = ['yt', 'xr', 'a', 'e', 'i', 'o', 'u']
    consonant_clusters = ['thr', 'squ', 'sch', 'rh', 'ch', 'qu', 'th']
    text = text.split()
    result = ''
    for word in text:
        word_as_list = list(word)
        if first_char_checker(word, vowels_and_consonants_treated_as_vowels) is None:
            first_chars = first_char_checker(word, consonant_clusters)
            if first_chars is not None:
                first_two_chars = "".join(word_as_list[:len(first_chars)])
                word_as_list = word_as_list[len(first_chars):len(word_as_list)]
                word_as_list.append(first_two_chars)
            else:
                first_char = word_as_list.pop(0)
                word_as_list.append(first_char)
        result += "".join(word_as_list) + "ay "
    return result.strip()

def first_char_checker(text, list):
    for cons in list:
        if text.startswith(cons):
            return cons
    return None
