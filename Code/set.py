from hashtable import HashTable


class Set:
    def __init__(self, elements=None):
        """Initialize this new set and add the given elements"""
        self.hash_set = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def size(self):
        """Returns the size of the set"""
        return self.hash_set.size

    def contains(self, element):
        """Return True if the set contains the given element, or False.
        Running time: 0(1); hash tables automatically resize"""
        return self.hash_set.contains(element)

    def add(self, element):
        """Add given element to the set, if not already present
        Running time: 0(1); adds key-value pair at constant time"""
        if not self.hash_set.contains(element):
            self.hash_set.set(element, 1)

    def remove(self, element):
        """Remove the given element from the set, if exists, or raise KeyError
        Running time: 0(1); jump right to element using key & remove -- constant time"""
        if self.hash_set.contains(element):
            self.hash_set.delete(element)
        else:
            raise KeyError(f'Item not found: {element}')

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set
        Running time: 0(m+n); gets keys, possible resizing needed, adds to new set"""
        new_set = Set()

        t_set = self.hash_set.keys()
        o_set = other_set.hash_set.keys()

        for element in t_set:
            new_set.add(element)
        for element in o_set:
            new_set.add(element)

        return new_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set
        Running time: 0(n); gets keys linearly"""
        new_set = Set()

        o_set = other_set.hash_set.keys()

        for element in o_set:
            if self.contains(element):
                new_set.add(element)

        return new_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set
        Running time: 0(n); gets keys linearly"""
        new_set = Set()

        t_set = self.hash_set.keys()
        o_set = other_set.hash_set.keys()

        for element in t_set:
            if other_set.contains(element) is False:
                new_set.add(element)
        for element in o_set:
            if self.contains(element) is False:
                new_set.add(element)

        return new_set

    def is_subset(self, other_set):
        """Return True if other_set is a subset of this set, or False
        Running time: 0(n); gets keys linearly"""
        t_set = self.hash_set.keys()
        o_set = other_set.hash_set.keys()

        for element in o_set:
            if element not in t_set:
                return False

        return True
