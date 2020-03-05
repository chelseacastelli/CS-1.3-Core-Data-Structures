
from load_dictionary import read_in_data
import os
from subprocess import call

jumble_dict = dict()

def unjumble_key(word):
    """Return a string that is the unjumble key of its input"""
    return "".join(sorted(word))

def make_unjumble_dict(words):
    """Create a jumbled key for every word in 'dict' file & append its anagrams as values []"""
    for word in words:
        word = word.lower()
        sort_wrd = unjumble_key(word)
        jumble_dict.setdefault(sort_wrd, []).append(word)

def unjumble(word):
    """Returns a list of all words in the dictionary to which the input string unjumbles"""
    return jumble_dict["".join(sorted(word))]


def clear():
    '''A function that clears the terminal for better readability'''
    _ = call('clear' if os.name =='posix' else 'cls')


if __name__ == "__main__":
    words = []

    arr = read_in_data('/usr/share/dict/words')
    make_unjumble_dict(arr)

    print("-----WELCOME TO JUMBLE!-----\n")

    num = input("How many words are you going to enter? ")

    for _ in range(int(num)):
        words.append(input("Please input a jumble word: "))

    clear()

    print("\n-----SOLVED!-----\n")

    for word in words:
        print(f'{word} --> {unjumble(word)[0]}')

    print('\n')
