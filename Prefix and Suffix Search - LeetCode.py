import collections
from typing import List

from structures.trie import Trie, trie_put_for_every_letter, trie_put, trie_get


class WordFilter(object):
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.words = words

        for weight, word in enumerate(words):
            key = word + '#' + word
            for i in range(len(word) + 1):
                key_to_put = ''
                for letter in key[i:]:
                    key_to_put += letter
                    trie_put(self.trie, key_to_put, weight)

    def f(self, prefix: str, suffix: str):
        if not prefix and not suffix:
            return len(self.words) - 1
        return trie_get(self.trie, suffix + '#' + prefix, -1)


def test_one(words: List[str], prefixes: List[List[str]]):
    print(words)
    fl = WordFilter(words)

    for prefix, suffix in prefixes:
        print('"{}" "{}"'.format(prefix, suffix))
        print(fl.f(prefix, suffix))


if __name__ == '__main__':
    test_one(
        ["pop"],
        [["", ""], ["", "p"], ["", "op"], ["", "pop"], ["p", ""], ["p", "p"], ["p", "op"], ["p", "pop"], ["po", ""],
         ["po", "p"], ["po", "op"], ["po", "pop"], ["pop", ""], ["pop", "p"], ["pop", "op"], ["pop", "pop"], ["", ""],
         ["", "p"], ["", "gp"], ["", "pgp"], ["p", ""], ["p", "p"], ["p", "gp"], ["p", "pgp"], ["pg", ""], ["pg", "p"],
         ["pg", "gp"], ["pg", "pgp"], ["pgp", ""], ["pgp", "p"], ["pgp", "gp"], ["pgp", "pgp"]]
    )
