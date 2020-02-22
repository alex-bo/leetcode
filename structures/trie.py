import collections
from typing import Any, List

Trie = lambda: collections.defaultdict(Trie)

TRIE_VALUE_SLOT = '__value__'
TRIE_WILDCARD_DOT = '.'


def trie_put(trie: Trie, key: str, value: Any):
    if not key:
        raise KeyError('Key cannot be None or empty.')
    for letter in key:
        trie = trie[letter]
    trie[TRIE_VALUE_SLOT] = value


def trie_put_for_every_letter(trie: Trie, key: str, value: Any):
    if not key:
        raise KeyError('Key cannot be None or empty.')
    for letter in key:
        trie = trie[letter]
        trie[TRIE_VALUE_SLOT] = value


def trie_get(trie: Trie, key: str, default: Any = None) -> Any:
    if not key:
        raise KeyError('Key cannot be None or empty.')
    for letter in key:
        if letter not in trie:
            return default
        trie = trie[letter]
    return trie[TRIE_VALUE_SLOT]


def trie_get_wildcard(trie: Trie, key: str) -> List[Any]:
    if not key:
        raise KeyError('Key cannot be None or empty.')
    curr_tries, next_tries = [trie], []
    for letter in key:
        if not curr_tries:
            break
        next_tries.clear()
        for trie in curr_tries:
            if letter == TRIE_WILDCARD_DOT:
                for k, v in trie.items():
                    if k != TRIE_VALUE_SLOT:
                        next_tries.append(v)
            elif letter in trie:
                next_tries.append(trie[letter])
        curr_tries, next_tries = next_tries, curr_tries
    return [
        trie[TRIE_VALUE_SLOT] for trie in curr_tries if TRIE_VALUE_SLOT in trie
    ]


class TSTNode:

    def __init__(self):
        self.left = None
        self.mid = None
        self.right = None
        self.char = None
        self.value = None


class TernarySearchTrie:

    def __init__(self):
        self.root = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def __delitem__(self, item: str):
        val = self.get(item)
        if val is None:
            raise KeyError(item)
        self.put(item, None)

    def __bool__(self):
        return self.__count > 0

    def __getitem__(self, item: str):
        val = self.get(item)
        if val is None:
            raise KeyError(val)
        return val

    def __contains__(self, item: str):
        return self.get(item) is not None

    def __setitem__(self, key: str, value: Any):
        self.put(key, value)

    def put(self, key: str, value: Any):
        if not key:
            raise ValueError('Empty key is not supported.')
        self.root = self.__put(self.root, key, value, 0)

    def __put(self, x: TSTNode, key: str, value: Any, depth: int) -> TSTNode:
        c = key[depth]

        # create new node
        if not x:
            x = TSTNode()
            x.char = c

        if c < x.char:
            # proceed left
            x.left = self.__put(x.left, key, value, depth)
        elif c > x.char:
            # proceed right
            x.right = self.__put(x.right, key, value, depth)
        elif depth < (len(key) - 1):
            # character match and it's not the last one in the key
            x.mid = self.__put(x.mid, key, value, depth + 1)
        else:
            # character match and it's the last one in the key
            if not x.value and value:
                self.__count += 1
            elif x.value and not value:
                self.__count -= 1
            x.value = value

        return x

    def get(self, key: str, default: Any = None) -> Any:
        if not key:
            return None
        val = self.__get(self.root, key, 0)
        if val is None:
            return default
        return val

    def __get(self, x: TSTNode, key: str, depth: int):
        if not x:
            return None

        c = key[depth]

        if c < x.char:
            return self.__get(x.left, key, depth)
        elif c > x.char:
            return self.__get(x.right, key, depth)
        elif depth < (len(key) - 1):
            return self.__get(x.mid, key, depth + 1)

        return x.value

