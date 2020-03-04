
from pprint import pprint
import random
from load_dictionary import read_in_data

jumble_dict = dict()

def unjumble_key(word):
    return "".join(sorted(word))

def make_unjumble_dict(words):
    """Create a jumbled key for every word in 'dict' file & append its anagrams as values []"""
    for word in words:
        sort_wrd = unjumble_key(word)
        jumble_dict.setdefault(sort_wrd, []).append(word)

def unjumble(word):
    return jumble_dict[word]


# def random_words(words, num_words):
#     rand_w = []
#     for i in range(num_words):
#         rand_i = random.randrange(len(words) - 1)
#         rand_w.append(words[rand_i])


if __name__ == "__main__":
    # '/usr/share/dict/words'
    # ['cat', 'car', 'listen', 'taco', 'silent']
    # arr = read_in_data('/usr/share/dict/words')
    make_unjumble_dict(['cat', 'car', 'shrub', 'rats', 'star', 'arts', 'regal', 'listen', 'taco', 'silent', 'brush'])
    pprint(jumble_dict)


