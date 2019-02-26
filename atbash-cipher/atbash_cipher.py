import string

class Atbash():

    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)
        self.reversed_alphabet = list(reversed(self.alphabet))

    def encode(self, plain_text):
        result = ''
        plain_text = plain_text.replace(' ', '')
        num_of_processed_chars = 0
        for i in range(0, len(plain_text)):
            if plain_text[i].isalpha():
                index_of_char = self.alphabet.index(plain_text[i].lower())
                result += self.reversed_alphabet[index_of_char]
                num_of_processed_chars += 1
            elif plain_text[i].isdigit():
                result += plain_text[i]
                num_of_processed_chars += 1
            else:
                pass
            if num_of_processed_chars == 5:
                result += ' '
                num_of_processed_chars = 0
        return result.strip()

    def decode(self, ciphered_text):
        result = ''
        ciphered_text = ciphered_text.replace(' ', '')
        for i in range(0, len(ciphered_text)):
            if ciphered_text[i].isalpha():
                result += self.alphabet[self.reversed_alphabet.index(ciphered_text[i])]
            else:
                result += ciphered_text[i]
        return result