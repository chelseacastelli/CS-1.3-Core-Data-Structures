from hashtable import HashTable


class Set:
    def __init__(self, elements=None):
        """Initialize this new set and add the given elements"""
        self.hash_set = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def size(self):
        """Returns the size of the set
        Running time: 0(1);
        Space (memory): """
        return self.hash_set.size

    def contains(self, element):
        """Return True if the set contains the given element, or False.
        Running time: ;
        Space (memory): """
        pass

    def add(self, element):
        """Add given element to the set, if not already present
        Running time: ;
        Space (memory):
        """
        pass

    def remove(self, element):
        """Remove the given element from the set, if exists, or raise KeyError
        Running time: ;
        Space (memory):
        """
        pass

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set
        Running time: ;
        Space (memory): """
        pass

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set
        Running time: ;
        Space (memory): """
        pass

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set
        Running time: ;
        Space (memory): """
        pass

    def is_subset(self, other_set):
        """Return True if other_set is a subset of this set, or False
        Running time: ;
        Space (memory): """
        pass