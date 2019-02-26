def is_isogram(string):
    split_word = list(filter(lambda character: character.isalpha(), list(string.upper())))
    set_split_word = set(split_word)
    return len(split_word) == len(set_split_word)