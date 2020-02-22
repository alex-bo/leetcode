from structures.trie import Trie as TrieDict, trie_put, trie_get, trie_put_for_every_letter


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.search_trie = TrieDict()
        self.starts_with_trie = TrieDict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie_put(self.search_trie, word, True)
        trie_put_for_every_letter(self.starts_with_trie, word, True)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return trie_get(self.search_trie, word, False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return trie_get(self.starts_with_trie, prefix, False)


if __name__ == '__main__':
    t = Trie()
    t.insert('test')
    t.insert('hello')
    t.insert('hell')
    t.insert('help')
    t.search('hello')
    t.startsWith('hel')
