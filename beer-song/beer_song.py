def recite(start, take=1):
    iteration = take
    counter = start
    list_of_lirycs_lines = []
    while iteration > 0:
        if counter > 2:
            first_part = "{0} bottles of beer on the wall, {1} bottles of beer.".format(counter, counter)
            second_part = "Take one down and pass it around, {0} bottles of beer on the wall.".format(counter-1)
        elif counter == 2:
            first_part = "{0} bottles of beer on the wall, {1} bottles of beer.".format(counter, counter)
            second_part = "Take one down and pass it around, {0} bottle of beer on the wall.".format(counter-1)
        elif counter == 1:
            first_part = "{0} bottle of beer on the wall, {1} bottle of beer.".format(counter, counter)
            second_part = "Take it down and pass it around, no more bottles of beer on the wall."
        else:
            first_part = "No more bottles of beer on the wall, no more bottles of beer."
            second_part = "Go to the store and buy some more, 99 bottles of beer on the wall."
        iteration -= 1
        counter -= 1
        list_of_lirycs_lines.append(first_part)
        list_of_lirycs_lines.append(second_part)
        if iteration > 0:
            list_of_lirycs_lines.append('')
    return list_of_lirycs_lines