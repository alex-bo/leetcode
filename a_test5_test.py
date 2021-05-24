#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#

import collections, heapq
from typing import List

Trie = lambda: collections.defaultdict(Trie)
TRIE_VALUE_SLOT = '__value__'


def trie_put(trie: Trie, word: str, query: str):
    depth = 0
    for w_letter, q_letter in zip(word, query):
        if w_letter != q_letter:
            break
        depth += 1
        trie = trie[w_letter]
        if depth >= 2:
            if TRIE_VALUE_SLOT not in trie:
                trie[TRIE_VALUE_SLOT] = []
            heapq.heappush(trie[TRIE_VALUE_SLOT], word)


def trie_get(trie: Trie, query: str) -> List[List[str]]:
    depth = 0
    result = []
    for letter in query:
        depth += 1
        trie = trie[letter]
        if depth >= 2:
            result.append(heapq.nsmallest(3, trie[TRIE_VALUE_SLOT]))
    return result


def searchSuggestions(repository, customerQuery):
    trie = Trie()
    for word in repository:
        trie_put(trie, word, customerQuery)

    return trie_get(trie, customerQuery)


if __name__ == '__main__':
    print(searchSuggestions(
        [
            'bags',
            'baggage',
            'banner',
            'box',
            'cloths',
         ],
        'bags'
    ))
