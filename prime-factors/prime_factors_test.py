import unittest

from prime_factors import prime_factors


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class PrimeFactorsTest(unittest.TestCase):
    def test_no_factors(self):
        self.assertEqual(prime_factors(1), [])

    def test_prime_number(self):
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(13), [13])

    def test_square_of_a_prime(self):
        self.assertEqual(prime_factors(9), [3, 3])

    def test_cube_of_a_prime(self):
        self.assertEqual(prime_factors(8), [2, 2, 2])

    def test_product_of_primes_and_non_primes(self):
        self.assertEqual(prime_factors(6), [2, 3])
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(147), [3, 7, 7])
        self.assertEqual(prime_factors(330), [2, 3, 5, 11])
        self.assertEqual(prime_factors(343), [7, 7, 7])
        self.assertEqual(prime_factors(552), [2, 2, 2, 3, 23])
        self.assertEqual(prime_factors(32767), [7, 31, 151])
        self.assertEqual(prime_factors(48), [2, 2, 2, 2, 3])


    # def test_product_of_primes(self):
    #     self.assertEqual(prime_factors(901255), [5, 17, 23, 461])
    #
    # def test_factors_include_a_large_prime(self):
    #     self.assertEqual(prime_factors(93819012551), [11, 9539, 894119])


if __name__ == '__main__':
    unittest.main()
