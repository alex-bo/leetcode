import collections

from structures.trie import Trie, trie_put, trie_get_wildcard


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie_put(self.trie, word, True)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return bool(trie_get_wildcard(self.trie, word))


if __name__ == '__main__':
    d = WordDictionary()
    d.addWord('bad')
    d.addWord('dad')
    d.addWord('mad')
    print("d.search('pad') -> {}".format(d.search('pad')))
    print("d.search('bad') -> {}".format(d.search('bad')))
    print("d.search('.ad') -> {}".format(d.search('.ad')))
    print("d.search('b..') -> {}".format(d.search('b..')))
    print("d.search('b') -> {}".format(d.search('b')))
