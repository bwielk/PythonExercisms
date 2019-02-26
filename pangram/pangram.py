import string

def is_pangram(sentence):
    if isinstance(sentence, str):
        all_chars = list(map(chr, range(ord('a'), ord('z')+1)))
        sentence = sentence.lower().replace(" ", "")
        for ch in sentence:
            if all_chars.__contains__(ch):
                all_chars.remove(ch)
            else:
                pass
        if len(all_chars) == 0:
            return True
        return False
    raise TypeError("The sentence should be a string e.g. 'Alice has a cat'")

