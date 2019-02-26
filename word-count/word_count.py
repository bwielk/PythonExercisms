import re

def word_count(phrase):
    string_without_non_alpha = re.sub("[^a-zA-Z0-9']+", " ", phrase)
    list_of_words = string_without_non_alpha.split(" ")
    list_of_words = map(lambda x: x.lower().strip("'"), filter(lambda word: len(word) > 0, list_of_words))
    dict_of_words = {}
    for word in list_of_words:
        if dict_of_words.__contains__(word):
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1
    return dict_of_words