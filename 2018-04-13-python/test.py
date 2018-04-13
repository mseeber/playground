"""
Unit tests for primenumber module
"""

import unittest

import primenumber

#no docstrings strictly required here
#pylint: disable=C0111
class PrimeCheck(unittest.TestCase):

    def setUp(self):
        self.prime_set = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
        self.not_prime_set = set([0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20,
                                  21, 22])


    def test_is_prime(self):
        for n in self.prime_set:
            with self.subTest(n=n):
                self.assertTrue(primenumber.is_prime(n))


    def test_is_not_prime(self):
        for n in self.not_prime_set:
            with self.subTest(n=n):
                self.assertFalse(primenumber.is_prime(n))


    def test_large_number_is_prime(self):
        self.assertTrue(primenumber.is_prime((2 ** 17) - 1))


    def test_large_number_is_not_prime(self):
        self.assertFalse(primenumber.is_prime(2 ** 17))

    #@unittest.skip("only run this when you have too much time")
    def test_product_of_large_primes(self):
        self.assertFalse(primenumber.is_prime(100032997 * 100033009))


class PrimeIndex(unittest.TestCase):

    def setUp(self):
        self.primes_ordered = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

    def test_index_matches(self):

        for i, p in enumerate(self.primes_ordered):
            with self.subTest(prime=p, index=i):
                self.assertEqual(primenumber.get_number(i), p)

    def test_get_numbers_length(self):
        for c in [0, 1, 2, 3, 5, 10, 33]:
            with self.subTest(numbers_requested=c):
                result = primenumber.get_numbers(c)
                self.assertEqual(len(result), c)

    def test_get_numbers(self):
        for c in [0, 1, 2, 3, 5, 7, 14]:
            with self.subTest(numbers_requested=c):
                self.assertEqual(self.primes_ordered[:c],
                                 primenumber.get_numbers(c))


if __name__ == '__main__':
    unittest.main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
