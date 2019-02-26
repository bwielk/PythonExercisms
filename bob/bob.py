def hey(phrase):
    phrase = phrase.strip().replace(' ', '')
    print(phrase)
    if any(char.isalnum() for char in phrase) or phrase.endswith(('?', '!')):
        if phrase.endswith('?'):
            if phrase[:-1].isupper():
                return 'Calm down, I know what I\'m doing!'
            return 'Sure.'
        if phrase[:-1].upper() == phrase[:-1] and any(char.isalpha() for char in phrase):
            return 'Whoa, chill out!'
        return 'Whatever.'
    return 'Fine. Be that way!'