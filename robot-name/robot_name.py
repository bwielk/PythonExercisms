import random

class Robot(object):
    def __init__(self):
        self.name = self.__generate_robot_name()
        print(self.name)

    def __generate_robot_name(self):
        first_letter = self.__generate_random_character()
        second_letter = self.__generate_random_character()
        first_digit = self.__generate_random_digit_string()
        second_digit = self.__generate_random_digit_string()
        third_digit = self.__generate_random_digit_string()
        return first_letter + second_letter + first_digit + second_digit + third_digit

    def __generate_random_character(self):
        return chr(random.randint(ord('a'), ord('z'))).upper()

    def __generate_random_digit_string(self):
        return str(random.randint(0,9))

    def reset(self):
        new_name = self.__generate_robot_name()
        if new_name == self.name:
            self.name = self.__generate_robot_name()
        else:
            self.name = new_name
