#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
LETTERS = string.ascii_letters

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text, 0, len(text)-1)


def is_palindrome_iterative(text):
    starting_index = 0
    ending_index = len(text) - 1

    text.lower()

    while text:
        if starting_index == ending_index:
            return True
        while not text[starting_index].isalpha():
            starting_index += 1
        while not text[ending_index].isalpha():
            ending_index += 1
        if text[starting_index] == text[ending_index]:
            starting_index += 1
            ending_index -= 1
        else:
            return False


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here

    if left is None and right is None:
        left = 0
        right = len(text) - 1

    while True:
        if left == right:
            return True
        elif text[left] == text[right]:
            return is_palindrome_recursive(text, left+1, right-1)
        else:
            return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('\n{}: {} {} a palindrome\n'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
