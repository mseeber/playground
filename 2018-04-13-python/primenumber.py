"""
A collection of functions in regards to prime numbers.
"""

import math
import functools

def _sqrt(number):
    """
    @return the rounded up square root of @parameter number
    """

    return math.ceil(math.sqrt(number))

@functools.lru_cache(maxsize=32, typed=False)
def is_prime(number):
    """
    @return True if @parameter number is a prime number, false if not.
    """

    if number < 2:
        return False

    if number == 2:
        return True

    if (number % 2) == 0:
        return False

    inclusive_sieve_range = lambda start, end: range(start, end+1, 2)
    for n in inclusive_sieve_range(3, _sqrt(number)):
        if number % n == 0:
            return False

    # if there are no prime factors it is a prime number
    return True


def get_number(index):
    """
    @return the n-th prime (zero index) number assumes n >= 0

    at least n * sqrt(n)
    """
    candidate = 2
    while index > 0:
        index -= 1
        candidate += 1
        while not is_prime(candidate):
            candidate += 1

    return candidate


def get_numbers(count):
    """
    @return the first n prime numbers
    """
    numbers = []

    for i in range(0, count):
        numbers.append(get_number(i))

    return numbers

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
