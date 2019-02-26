def encode(plain_text):
    result = []
    prepared_word = ''.join(list(filter(lambda x: x.isalnum(), plain_text))).lower()
    square_root_of_prepared_word = int(len(prepared_word)**0.5)
    if square_root_of_prepared_word > 1 and len(plain_text) > 2:
        start_of_the_word_split = 0
        for i in range(1, square_root_of_prepared_word+1):
            result.append(prepared_word[start_of_the_word_split:start_of_the_word_split + square_root_of_prepared_word])
            start_of_the_word_split += square_root_of_prepared_word
    else:
        return prepared_word
    encryption = []
    for x in range(0, square_root_of_prepared_word):
        encryption.append(''.join([char[x] for char in result]))
    return ' '.join(encryption)
