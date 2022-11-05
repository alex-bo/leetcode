from typing import List, Set

from collections import defaultdict

Trie = lambda: defaultdict(Trie)
TRIE_SLOT = '__SLOT__'


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = set()
        trie = Trie()
        rev_trie = Trie()
        blank_words = set()
        for i, w in enumerate(words):
            trie_put(trie, w, i)
            trie_put(rev_trie, w[::-1], i)
            if not w:
                blank_words.add(i)
        for i, w in enumerate(words):
            st = blank_words.copy()
            trie_collect(trie, st, w[::-1])
            trie_collect(rev_trie, st, w)
            for j in st:
                if i == j:
                    continue
                if is_palindrome(words[i], words[j]):
                    res.add((i, j))
                if is_palindrome(words[j], words[i]):
                    res.add((j, i))
        return [[i, j] for i, j in res]


def is_palindrome(word1: str, word2: str) -> bool:
    return (
            (word1 + word2) == (word1 + word2)[::-1]
    )


def trie_put(trie: Trie, word: str, i: int) -> None:
    tr = trie
    for w in word:
        tr = tr[w]
    if TRIE_SLOT not in tr:
        tr[TRIE_SLOT] = []
    tr[TRIE_SLOT].append(i)


def trie_collect(trie: Trie, st: Set[int], word: str = '') -> None:
    tr = trie
    for w in word:
        if w not in tr:
            return
        tr = tr[w]
    for k, v in tr.items():
        if k == TRIE_SLOT:
            for i in tr[k]:
                st.add(i)
        else:
            trie_collect(v, st)


if __name__ == '__main__':
    print([[0, 1], [1, 0], [3, 2], [2, 4]])
    print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
