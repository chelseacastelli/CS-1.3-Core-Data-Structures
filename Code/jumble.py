
import random
import sys

dict_words = []
anagrams = []


def find_anagrams(words):
    for word in words:
        for other_word in words:
            if sorted(word) == sorted(other_word):
                anagrams.append(word)
                anagrams.append(other_word)


if __name__ == '__main__':
    dict_words = read_in_data('/usr/share/dict/words')
    # print(words)
    find_anagrams(dict_words)
    print(anagrams)
