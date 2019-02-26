class Luhn(object):
    def __init__(self, card_num):
        self.card_num = list(card_num.replace(' ', ''))
        self.checked_if_is_valid = False

    def is_valid(self):
        if (all(isinstance(digit, int) for digit in self.card_num) or all(digit.isdigit() for digit in self.card_num))\
                and self.checked_if_is_valid is False:
            self.card_num = self._turn_list_of_chars_into_list_of_ints(self.card_num)
            self.card_num = self._double_every_second_int_from_right_to_left(self.card_num)
            return self._validate_the_card_number(self.card_num)
        else:
            return self.checked_if_is_valid

    def _turn_list_of_chars_into_list_of_ints(self, list_to_convert):
        return list(map(lambda x: int(x), list_to_convert))

    def _double_every_second_int_from_right_to_left(self, list_of_ints):
        for i in range(len(list_of_ints) - 1, 1, -2):
            num_to_double = list_of_ints[i - 1]
            if num_to_double * 2 > 9:
                list_of_ints[i - 1] = num_to_double * 2 - 9
            else:
                list_of_ints[i - 1] = num_to_double * 2
        return list_of_ints

    def _validate_the_card_number(self, list_of_ints):
        if sum(list_of_ints) % 10 == 0 and len(list_of_ints) > 1:
            self.checked_if_is_valid = True
            return True
        else:
            return False