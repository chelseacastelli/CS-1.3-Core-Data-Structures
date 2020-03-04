from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        hash_set = Set(['i', 'm', 's', 'a', 'd'])
        assert hash_set.size() == 5

    def test_contains(self):
        hash_set = Set(['a', 'b', 'c'])
        assert hash_set.contains('a') == True
        assert hash_set.contains('b') == True
        assert hash_set.contains('c') == True
        assert hash_set.contains('e') == False
        assert hash_set.contains('d') == False

    def test_add(self):
        hash_set = Set()
        hash_set.add('a') == True
        hash_set.add('b') == True
        hash_set.add('c') == True
        assert hash_set.size() == 3

    def test_remove(self):
        hash_set = Set()
        hash_set.add('p')
        hash_set.add('j')
        assert hash_set.size() == 2
        hash_set.remove('j')
        assert hash_set.size() == 1

    def test_union(self):
        set1 = Set(['l', 'm', 'n'])
        set2 = Set(['o', 'p', 'q'])
        set3 = set1.union(set2)
        assert set3.contains('l') == True
        assert set3.contains('m') == True
        assert set3.contains('n') == True
        assert set3.contains('q') == True
        assert set3.size() == 6

        set1 = Set(['C', 'H', 'E'])
        set2 = Set(['L', 'S'])
        set3 = set1.union(set2)
        assert set3.contains('H') == True
        assert set3.contains('E') == True
        assert set3.contains('C') == True
        assert set3.contains('L') == True
        assert set3.contains('S') == True
        assert set3.size() == 5

        set1 = Set([12, 24])
        set2 = Set([11, 7])
        set3 = set1.union(set2)
        assert set3.contains(7) == True
        assert set3.contains(12) == True
        assert set3.contains(13) == False
        assert set3.size() == 4

    def test_intersection(self):
        set1 = Set(['a', 's', 'h'])
        set2 = Set(['h', 'o', 't'])
        set3 = set1.intersection(set2)
        assert set3.contains('h') == True
        assert set3.size() == 1

        set4 = Set(['B', 'A', 'E'])
        set5 = Set(['S', 'L', 'A', 'Y'])
        set6 = set5.intersection(set4)
        assert set6.contains('A') == True
        assert set6.size() == 1

        set7 = Set([4, 20, 5])
        set8 = Set([2, 8, 20])
        set9 = set7.intersection(set8)
        assert set9.contains(20) == True
        assert set9.size() == 1

    def test_difference(self):
        set1 = Set(['y', 'o', 'u'])
        set2 = Set(['f', 'i', 'n', 'e'])
        set3 = set1.difference(set2)
        assert set3.contains('o') == True
        assert set3.contains('u') == True
        assert set3.contains('i') == True
        assert set3.contains('e') == True
        assert set3.size() == 7

        set4 = Set(['S', 'U', 'G', 'A', 'R'])
        set5 = Set(['L', 'I', 'P'])
        set6 = set4.difference(set5)
        assert set6.contains('U') == True
        assert set6.contains('A') == True
        assert set6.contains('R') == True
        assert set6.contains('I') == True
        assert set6.size() == 8

        set7 = Set([0, 8, 7])
        set8 = Set([6, 10, 9])
        set9 = set7.difference(set8)
        assert set9.contains(0) == True
        assert set9.contains(6) == True
        assert set9.size() == 6

    def test_is_subset(self):
        set1 = Set(['y', 'e', 'a'])
        set2 = Set(['n', 'o'])
        assert set1.is_subset(set2) == False

        set3 = Set(['B', 'A', 'E'])
        set4 = Set(['B', 'A'])
        assert set3.is_subset(set4) == True

        set5 = Set([1234, 23456, 345678])
        set6 = Set([1234, 23456])
        assert set5.is_subset(set6) == True


if __name__ == '__main__':
    unittest.main()