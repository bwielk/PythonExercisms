def abbreviate(words):
    list_of_words = words.replace('-', ' ').split(' ')
    list_without_unnecessary_spaces = filter(lambda el: el != '', list_of_words)
    first_chars = [word[0] for word in list_without_unnecessary_spaces]
    return ''.join(first_chars).upper()