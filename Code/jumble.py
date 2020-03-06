
from load_dictionary import read_in_data
import os
from subprocess import call


class DictUnjumble(object):
    def __init__(self):
        self.dictionary = dict()

    def unjumble_key(self, word):
        """Return a string that is the unjumble key of its input"""
        return "".join(sorted(word))

    def make_unjumble_dict(self, words):
        """Create a jumbled key for every word in 'dict' file & append its anagrams as values []"""
        for word in words:
            word = word.lower()
            sort_wrd = self.unjumble_key(word)
            self.dictionary.setdefault(sort_wrd, []).append(word)

    def unjumble(self, word):
        """Returns a list of all words in the dictionary to which the input string unjumbles"""
        w = "".join(sorted(word)).lower()
        if w in self.dictionary:
            return self.dictionary[w]
        raise KeyError(f'{word} not in dictionary')


def clear():
    """A function that clears the terminal for better readability"""
    _ = call('clear' if os.name =='posix' else 'cls')


if __name__ == "__main__":
    jumble = DictUnjumble()
    inputted_words = []

    dict_words = read_in_data('/usr/share/dict/words')
    jumble.make_unjumble_dict(dict_words)

    print("-----WELCOME TO JUMBLE!-----\n")
    num = input("How many words are you going to enter? ")
    print('\n')

    for _ in range(int(num)):
        inputted_words.append(input("Please input a jumble word: "))

    clear()

    print("\n-----SOLVED!-----\n")

    for word in inputted_words:
        print(f'{word} --> {jumble.unjumble(word)[0]}')

    print('\n')
