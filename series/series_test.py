"""Tests for the series exercise

Implementation note:
The slices function should raise a ValueError with a meaningful error
message if its length argument doesn't fit the series.
"""
import unittest

from series import slices, drop_zeros_in_the_beginning_of_a_number


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class SeriesTest(unittest.TestCase):
    def test_slices_of_one_from_one(self):
        self.assertEqual(slices("1", 1), ["1"])

    def test_slices_of_one_from_two(self):
        self.assertEqual(slices("12", 1), ["1", "2"])

    def test_slices_of_two(self):
        self.assertEqual(slices("35", 2), ["35"])

    def test_slices_of_two_overlap(self):
        self.assertEqual(slices("9142", 2), ["91", "14", "42"])

    def test_slices_can_include_duplicates(self):
        self.assertEqual(slices("777777", 3), ["777", "777", "777", "777"])

    def test_slices_can_deal_with_big_numbers(self):
        self.assertEqual(slices("1222912912831", 10), ["1222912912", "2229129128", "2291291283", "2912912831"])

    def test_dropping_zeros_in_the_beginning_of_number_works(self):
        self.assertEqual(drop_zeros_in_the_beginning_of_a_number("0001"), "1")
        self.assertEqual(drop_zeros_in_the_beginning_of_a_number("0121"), "121")
        self.assertEqual(drop_zeros_in_the_beginning_of_a_number("00301"), "301")
        self.assertEqual(drop_zeros_in_the_beginning_of_a_number("100121"), "100121")
        self.assertEqual(drop_zeros_in_the_beginning_of_a_number("0200100"), "200100")

    def test_slices_can_deal_with_big_numbers_and_get_rid_of_useless_0s_in_the_beginning_of_created_numbers(self):
        self.assertEqual(slices("1000120001", 5), ["10001", "12", "120", "1200", "12000", "20001"])

    def test_slice_length_is_too_large(self):
        with self.assertRaisesWithMessage(ValueError):
              slices("12345", 6)

    def test_slice_length_cannot_be_zero(self):
        with self.assertRaisesWithMessage(ValueError):
            slices("12345", 0)

    def test_slice_length_cannot_be_negative(self):
        with self.assertRaisesWithMessage(ValueError):
            slices("123", -1)

    def test_empty_series_is_invalid(self):
        with self.assertRaisesWithMessage(ValueError):
            slices("", 1)

    def test_does_not_accept_series_with_chars_other_than_digits(self):
        with self.assertRaisesWithMessage(ValueError):
            slices("123a3", 2)
        with self.assertRaisesWithMessage(ValueError):
            slices("l0123bba", 3)
        with self.assertRaisesWithMessage(ValueError):
            slices("series_of_digits", 4)

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
