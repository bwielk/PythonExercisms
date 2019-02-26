import unittest

from leap import is_leap_year


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

class LeapTest(unittest.TestCase):
    def test_year_not_divisible_by_4(self):
        self.assertIs(is_leap_year(2015), False)
        self.assertIs(is_leap_year(2016), True)

    def test_year_divisible_by_4_not_divisible_by_100(self):
        self.assertIs(is_leap_year(1996), True)

    def test_year_divisible_by_100_not_divisible_by_400(self):
        self.assertIs(is_leap_year(2100), False)
        self.assertIs(is_leap_year(2200), False)

    def test_year_divisible_by_400(self):
        self.assertIs(is_leap_year(2000), True)
        self.assertIs(is_leap_year(2400), True)

    def test_year_divisible_by_200_not_divisible_by_400(self):
        self.assertIs(is_leap_year(1800), False)

    def test_current_year_2018_is_not_a_leap_year(self):
        self.assertIs(is_leap_year(), False)

    def test_input_accepts_integer_parameters_only(self):
        self.assertRaises(TypeError, is_leap_year, "1902")


if __name__ == '__main__':
    unittest.main()
