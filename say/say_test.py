import unittest

from say import say


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class SayTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(say(0), "zero")

    def test_one_to_nine(self):
        self.assertEqual(say(1), "one")
        self.assertEqual(say(6), "six")
        self.assertEqual(say(8), "eight")

    def test_teens(self):
        self.assertEqual(say(11), "eleven")
        self.assertEqual(say(14), "fourteen")
        self.assertEqual(say(18), "eighteen")

    def test_whole_tens(self):
        self.assertEqual(say(10), "ten")
        self.assertEqual(say(20), "twenty")
        self.assertEqual(say(40), "forty")
        self.assertEqual(say(50), "fifty")
        self.assertEqual(say(90), "ninety")

    def test_21_to_99(self):
        self.assertEqual(say(21), "twenty-one")
        self.assertEqual(say(22), "twenty-two")
        self.assertEqual(say(65), "sixty-five")
        self.assertEqual(say(99), "ninety-nine")

    def test_whole_hundreds(self):
        self.assertEqual(say(100), "one hundred")
        self.assertEqual(say(500), "five hundred")
        self.assertEqual(say(900), "nine hundred")

    # additional track specific test
    def test_100_to_999(self):
        self.assertEqual(say(108), "one hundred and eight")
        self.assertEqual(say(311), "three hundred and eleven")
        self.assertEqual(say(523), "five hundred and twenty-three")
        self.assertEqual(say(850), "eight hundred and fifty")
        self.assertEqual(say(999), "nine hundred and ninety-nine")

    def test_1000_to_999999(self):
        self.assertEqual(say(1000), "one thousand")
        self.assertEqual(say(1234), "one thousand two hundred and thirty-four")
        self.assertEqual(say(9505), "nine thousand five hundred and five")
        self.assertEqual(say(10001), "ten thousand and one")
        self.assertEqual(say(100234), "one hundred thousand two hundred and thirty-four")
        self.assertEqual(say(440034), "four hundred and forty thousand and thirty-four")
        self.assertEqual(say(999999), "nine hundred and ninety-nine thousand nine hundred and ninety-nine")

    def test_1_000_000_to_999_999_999(self):
        self.assertEqual(say(1e6), "one million")
        self.assertEqual(
            say(1002345),
            "one million two thousand three hundred and forty-five")
        self.assertEqual(say(1010001), "one million ten thousand and one")
        self.assertEqual(say(55014021), "fifty-five million fourteen thousand and twenty-one")
        self.assertEqual(say(115004021), "one hundred and fifteen million four thousand and twenty-one")
        self.assertEqual(say(999999999), "nine hundred and ninety-nine million nine hundred"
                                         " and ninety-nine thousand nine hundred and ninety-nine")

    def test_one_billion(self):
        self.assertEqual(say(1e9), "one billion")

    def test_987654321123(self):
        self.assertEqual(
            say(987654321123), ("nine hundred and eighty-seven billion "
                                "six hundred and fifty-four million "
                                "three hundred and twenty-one thousand "
                                "one hundred and twenty-three"))

    def test_number_too_large(self):
        with self.assertRaisesWithMessage(ValueError):
            say(1e12)

    def test_number_negative(self):
        with self.assertRaisesWithMessage(ValueError):
            say(-1)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
