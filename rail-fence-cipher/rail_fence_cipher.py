index_distances = {2: [2, 1],
                   3: [4, 2, 4],
                   4: [6, 4, 2, 6],
                   5: [7, 5, 3, 2, 7],
                   6: [10, 8, 6, 4, 2, 10]}


def encode(message, rails):
    result = ''
    index = 0
    rail_index = 0
    if rails == 2:
        result += message[0::2]
        result += message[1::2]
    elif rails > 2 < 6:
        for i in index_distances[rails]:
            for x in range(0, len(message)):
                if index < len(message):
                    if rail_index > 0 < rails:
                        result += message[index]
                        index += i
                    else:
                        result += message[index]
                        index += i
                else:
                    rail_index += 1
                    index = rail_index
                    break
    return result


def decode(encoded_message, rails):
    pass
