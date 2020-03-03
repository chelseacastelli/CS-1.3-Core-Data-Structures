from set import Set
import unittest

class SetTests(unittest.TestCase):

    def __init__(self):
        hash_set = Set(['i', 'm', 's', 'a', 'd'])
        assert hash_set.size() == 5

