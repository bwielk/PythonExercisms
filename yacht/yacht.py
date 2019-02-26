# Score categories
# Change the values as you see fit

def four_of_a_kind(dice):
    for x in dice:
        if dice.count(x) >= 4:
            return x*4
        else:
            return 0

def full_house(dice):
    mapped_values = {}
    for x in dice:
        if x not in mapped_values.keys():
            mapped_values[x] = 1
        else:
            mapped_values[x] += 1
    if 3 in mapped_values.values() and 2 in mapped_values.values():
        return sum(dice)
    else:
        return 0

def extract_particular_int_and_sum_its_occurences(i):
    return lambda dice: sum(filter(lambda x: x == i, dice))

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = extract_particular_int_and_sum_its_occurences(1)
TWOS = extract_particular_int_and_sum_its_occurences(2)
THREES = extract_particular_int_and_sum_its_occurences(3)
FOURS = extract_particular_int_and_sum_its_occurences(4)
FIVES = extract_particular_int_and_sum_its_occurences(5)
SIXES = extract_particular_int_and_sum_its_occurences(6)
FULL_HOUSE = lambda dice: full_house(dice)
FOUR_OF_A_KIND = lambda dice: four_of_a_kind(dice)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda dice: sum(dice)

def score(dice, category):
    return category(dice)

