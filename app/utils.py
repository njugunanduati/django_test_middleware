import random


def get_random_digits(limit=6):
    """Generate random digits"""
    return "".join("{0}".format(n) for n in random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], limit))