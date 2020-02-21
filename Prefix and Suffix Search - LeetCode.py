from typing import List

from structures import RedBlackBST


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.l_bst = RedBlackBST()
        self.r_bst = RedBlackBST()
        for i, word in enumerate(self.words):
            self.l_bst[word] = i
            self.r_bst[word] = i

    def f(self, prefix: str, suffix: str) -> int:
        self.l_bst.select()


if __name__ == '__main__':
    obj = WordFilter(['apple', 'ale'])
    print("obj.f('a', 'e') = {}".format(obj.f('a', 'e')))

