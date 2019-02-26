def find_anagrams(word, candidates):
    if type(candidates) is list and type(word) is str:
        if all(word.lower() == candidate.lower() for candidate in candidates):
            return []
        word_to_compare = ''.join(sorted(word.lower()))
        return list(filter(lambda x: ''.join(sorted(x.lower())) == word_to_compare, candidates))
    else:
        raise ValueError('Incorrect method arguments.\
                        Word should be a string and candidates should be a list of strings')