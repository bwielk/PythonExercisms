def score(word):
    letter_values = dict({  1:  ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
                            2:  ["D", "G"],
                            3:  ["B", "C", "M", "P"],
                            4:  ["F", "H", "V", "W", "Y"],
                            5:  ["K"],
                            8:  ["J", "X"],
                            10: ["Z", "Q"]})
    number_of_points = 0
    for x,y in letter_values.items():
        for letter in word:
            if letter.upper() in y:
                number_of_points += x
    return number_of_points
