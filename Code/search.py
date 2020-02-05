#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Complexity: log2n
    array.sort()

    left = 0
    right = len(array) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        midpoint_value = array[midpoint]

        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    array.sort()

    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None
    else:
        midpoint = (left + right) // 2
        if item == array[midpoint]:
            return midpoint
        elif item < array[midpoint]:
            return binary_search_recursive(array, item, left, midpoint-1)
        else:
            return binary_search_recursive(array, item, midpoint+1, right)


if __name__ == '__main__':
    item = binary_search([1, 2, 3, 4, 8, 9, 5, 6, 7], 3)
    print(item)
