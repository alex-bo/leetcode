from typing import Any, Iterable, Optional, Iterator


# TODO: implement Graph, Try, Red-Black BST, Union-Find, etc.

# TODO: example of python structures usage


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


class RedBlackBSTNode:

    def __init__(self, key: Any, value: Any, is_red: bool, size: int):
        self.key = key
        self.value = value
        self.is_red = is_red
        self.size = size
        self.left = None
        self.right = None


class RedBlackBST:
    """
    Port of Red-Black Balanced Search Tree from Sedgewick's Algorithms course
    https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html
    """

    def __init__(self):
        self.root = None

    def __is_red(self, node: RedBlackBSTNode) -> bool:
        if node:
            return node.is_red
        return False

    def __size(self, node: RedBlackBSTNode) -> int:
        if node:
            return node.size
        return 0

    def __compare(self, key1: Any, key2: Any) -> int:
        if key1 > key2:
            return 1
        if key1 < key2:
            return -1
        return 0

    def __len__(self) -> int:
        """
        Returns the number of key-value pairs in this symbol table.
        :return: the number of key-value pairs in this symbol table
        """
        return self.__size(self.root)

    def __bool__(self) -> bool:
        """
        Is this symbol table empty?
        :return: True if this symbol table is empty and False otherwise
        """
        return self.root is not None

    def __getitem__(self, key: Any) -> Any:
        """
        Returns the value associated with the given key.
        :param key: the key
        :return: the value associated with the given key if the key is in the symbol table,
        raises KeyError if the key is not in the symbol table
        """
        val = self.get(key)
        if val is None:
            raise KeyError(key)
        return val

    def get(self, key: Any, default: Any = None) -> Optional[Any]:
        """
        Returns the value associated with the given key.
        :param key: the key
        :param default: default value if key not found
        :return: the value associated with the given key if the key is in the symbol table
        and None if the key is not in the symbol table
        """
        if key is None:
            raise KeyError('key is None')
        return self.__get(self.root, key) or default

    def __get(self, node: RedBlackBSTNode, key: Any) -> Optional[Any]:
        while node:
            cmp = self.__compare(key, node.key)
            if cmp < 0:
                node = node.left
            elif cmp > 0:
                node = node.right
            else:
                return node.value
        return None

    def __contains__(self, key: Any) -> bool:
        """
        Does this symbol table contain the given key?
        :param key: the key
        :return: True if this symbol table contains key and False otherwise
        """
        return self.get(key) is not None

    def __setitem__(self, key: Any, value: Any):
        """
        Inserts the specified key-value pair into the symbol table, overwriting the old
        value with the new value if the symbol table already contains the specified key.
        Deletes the specified key (and its associated value) from this symbol table
        if the specified value is None.
        :param key: the key
        :param value: the value
        """
        if key is None:
            raise KeyError('key is None')
        if value is None:
            del self[key]
            return
        self.root = self.__put(self.root, key, value)
        self.root.is_red = False

    def __put(self, node: RedBlackBSTNode, key: Any, value: Any) -> RedBlackBSTNode:
        if node is None:
            return RedBlackBSTNode(key, value, True, 1)
        cmp = self.__compare(key, node.key)
        if cmp < 0:
            node.left = self.__put(node.left, key, value)
        elif cmp > 0:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value

        # fix-up any right-leaning links
        if self.__is_red(node.right) and not self.__is_red(node.left):
            node = self.__rotate_left(node)
        if self.__is_red(node.left) and self.__is_red(node.left.left):
            node = self.__rotate_right(node)
        if self.__is_red(node.left) and self.__is_red(node.right):
            self.__flip_colors(node)
        node.size = self.__size(node.left) + self.__size(node.right) + 1

        return node

    def __rotate_left(self, node: RedBlackBSTNode) -> RedBlackBSTNode:
        x = node.right
        node.right = x.left
        x.left = node
        x.is_red = x.left.is_red
        x.left.is_red = True
        x.size = node.size
        node.size = self.__size(node.left) + self.__size(node.right) + 1
        return x

    def __rotate_right(self, node: RedBlackBSTNode) -> RedBlackBSTNode:
        x = node.left
        node.left = x.right
        x.right = node
        x.is_red = x.right.is_red
        x.right.is_red = True
        x.size = node.size
        node.size = self.__size(node.left) + self.__size(node.right) + 1
        return x

    def __flip_colors(self, node: RedBlackBSTNode):
        node.is_red = not node.is_red
        node.left.is_red = not node.left.is_red
        node.right.is_red = not node.right.is_red

    def __move_red_left(self, node: RedBlackBSTNode) -> RedBlackBSTNode:
        self.__flip_colors(node)
        if self.__is_red(node.right.left):
            node.right = self.__rotate_right(node.right)
            node = self.__rotate_left(node)
            self.__flip_colors(node)
        return node

    def __move_red_right(self, node: RedBlackBSTNode) -> RedBlackBSTNode:
        self.__flip_colors(node)
        if self.__is_red(node.left.left):
            node = self.__rotate_right(node)
            self.__flip_colors(node)
        return node

    def __balance(self, node: RedBlackBSTNode) -> RedBlackBSTNode:
        if self.__is_red(node.right):
            node = self.__rotate_left(node)
        if self.__is_red(node.left) and self.__is_red(node.left.left):
            node = self.__rotate_right(node)
        if self.__is_red(node.left) and self.__is_red(node.right):
            self.__flip_colors(node)

        node.size = self.__size(node.left) + self.__size(node.right) + 1
        return node

    def __delitem__(self, key: Any):
        """
        Removes the specified key and its associated value from this symbol table
        (if the key is in this symbol table).
        :param key: the key
        """
        if key not in self:
            return

        # if both children of root are black, set root to red
        if not self.__is_red(self.root.left) and not self.__is_red(self.root.right):
            self.root.is_red = True

        self.root = self.__delete(self.root, key)
        if self:
            self.root.is_black = False

    def __delete(self, node: RedBlackBSTNode, key: Any) -> Optional[Any]:
        if self.__compare(key, node.key) < 0:
            if not self.__is_red(node.left) and not self.__is_red(node.left.left):
                node = self.__move_red_left(node)
            node.left = self.__delete(node.left, key)
        else:
            if self.__is_red(node.left):
                node = self.__rotate_right(node)
            if self.__compare(key, node.key) == 0 and not node.right:
                return None
            if not self.__is_red(node.right) and not self.__is_red(node.right.left):
                node = self.__move_red_right(node)
            if self.__compare(key, node.key) == 0:
                x = self.__min(node.right)
                node.key = x.key
                node.val = x.value
                # node.val = get(node.right, min(node.right).key);
                # node.key = min(node.right).key;
                node.right = self.__delete_min(node.right)
            else:
                node.right = self.__delete(node.right, key)
        return self.__balance(node)

    def __delete_min(self, node: RedBlackBSTNode) -> Optional[RedBlackBSTNode]:
        if not node.left:
            return None

        if not self.__is_red(node.left) and not self.__is_red(node.left.left):
            node = self.__move_red_left(node)

        node.left = self.__delete_min(node.left)
        return self.__balance(node)

    def delete_min(self):
        """
        Removes the smallest key and associated value from the symbol table.
        """
        if not self:
            raise ValueError("BST underflow")

        # if both children of root are black, set root to red
        if not self.__is_red(self.root.left) and not self.__is_red(self.root.right):
            self.root.is_red = True

        self.root = self.__delete_min(self.root)
        if self:
            self.root.is_red = False

    def __delete_max(self, node: RedBlackBSTNode) -> Optional[RedBlackBSTNode]:
        if self.__is_red(node.left):
            node = self.__rotate_right(node)

        if not node.right:
            return None

        if not self.__is_red(node.right) and not self.__is_red(node.right.left):
            node = self.__move_red_right(node)

        node.right = self.__delete_max(node.right)

        return self.__balance(node)

    def delete_max(self):
        """
        Removes the largest key and associated value from the symbol table.
        """
        if not self:
            raise ValueError("BST underflow")

        # if both children of root are black, set root to red
        if not self.__is_red(self.root.left) and not self.__is_red(self.root.right):
            self.root.is_red = True

        self.root = self.__delete_max(self.root)
        if self:
            self.root.is_red = False

    def __min(self, node: RedBlackBSTNode) -> RedBlackBSTNode:
        if not node.left:
            return node
        else:
            return self.__min(node.left)

    def min(self) -> Any:
        """
        Returns the smallest key in the symbol table.
        """
        if not self:
            raise ValueError("calls min() with empty symbol table")
        return self.__min(self.root).key

    def __max(self, node: RedBlackBSTNode) -> RedBlackBSTNode:
        if not node.right:
            return node
        else:
            return self.__max(node.right)

    def max(self) -> Any:
        """
        Returns the largest key in the symbol table.
        :return: the largest key in the symbol table
        """
        if not self:
            raise ValueError("calls max() with empty symbol table")
        return self.__max(self.root).key

    def __floor(self, node: RedBlackBSTNode, key: Any) -> Optional[RedBlackBSTNode]:
        if not node:
            return None
        cmp = self.__compare(key, node.key)
        if cmp == 0:
            return node
        if cmp < 0:
            return self.__floor(node.left, key)
        t = self.__floor(node.right, key)
        if t:
            return t
        else:
            return node

    def floor(self, key: Any) -> Any:
        """
        Returns the largest key in the symbol table less than or equal to key.
        :param key: the key
        :return: the largest key in the symbol table less than or equal to key
        """
        if key is None:
            raise KeyError("argument to floor() is None")
        if not self:
            raise ValueError("calls floor() with empty symbol table")
        x = self.__floor(self.root, key)
        if not x:
            raise ValueError("argument to floor() is too small")
        else:
            return x.key

    def __ceiling(self, node: RedBlackBSTNode, key: Any) -> Optional[RedBlackBSTNode]:
        if not node:
            return None
        cmp = self.__compare(key, node.key)
        if cmp == 0:
            return node
        if cmp > 0:
            return self.__ceiling(node.right, key)
        t = self.__ceiling(node.left, key)
        if t:
            return t
        else:
            return node

    def ceiling(self, key: Any) -> Any:
        """
        Returns the smallest key in the symbol table greater than or equal to key.
        :param key: the key
        :return: the largest key in the symbol table less than or equal to key
        """
        if key is None:
            raise KeyError("argument to ceiling() is None")
        if not self:
            raise ValueError("calls ceiling() with empty symbol table")
        x = self.__ceiling(self.root, key)
        if not x:
            raise ValueError("argument to ceiling() is too large")
        else:
            return x.key

    def __select(self, node: RedBlackBSTNode, k: int) -> RedBlackBSTNode:
        t = self.__size(node.left)
        if t > k:
            return self.__select(node.left, k)
        elif t < k:
            return self.__select(node.right, k-t-1)
        else:
            return node

    def select(self, k: int) -> Any:
        """
        Return the key in the symbol table whose rank is k.
        This is the (k+1)st smallest key in the symbol table.

        :param k: the order statistic
        :return: the key in the symbol table of rank k
        """
        if k < 0 or k >= len(self):
            raise ValueError("argument to select() is invalid: " + str(k))
        x = self.__select(self.root, k)
        return x.key

    def __rank(self, key: Any, node: RedBlackBSTNode) -> int:
        if not node:
            return 0
        cmp = self.__compare(key, node.key)
        if cmp < 0:
            return self.__rank(key, node.left)
        elif cmp > 0:
            return 1 + self.__size(node.left) + self.__rank(key, node.right)
        else:
            return self.__size(node.left)

    def rank(self, key: Any) -> int:
        """
        Return the number of keys in the symbol table strictly less than key.
        :param key: the key
        :return: the number of keys in the symbol table strictly less than key
        """
        if key is None:
            raise KeyError("argument to rank() is null")
        return self.__rank(key, self.root)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.keys())

    def keys(self, low: Any = None, high: Any = None) -> Iterable[Any]:
        """
        Returns all keys in the symbol table in the given range, as an Iterable.
        :param low: minimum endpoint
        :param high: maximum endpoint
        :return: all keys in the symbol table between low (inclusive) and high (inclusive) as an Iterable
        """
        if low is None:
            low = self.min()
        if high is None:
            high = self.max()
        queue = []
        self.__keys(self.root, queue, low, high)
        return queue

    def __keys(self, node: RedBlackBSTNode, queue: list, low: Any, high: Any):
        if not node:
            return
        cmplo = self.__compare(low, node.key)
        cmphi = self.__compare(high, node.key)
        if cmplo < 0:
            self.__keys(node.left, queue, low, high)
        if cmplo <= 0 and cmphi >= 0:
            queue.append(node.key)
        if cmphi > 0:
            self.__keys(node.right, queue, low, high)

    def size(self, low: Any, high: Any) -> int:
        """
        Returns the number of keys in the symbol table in the given range
        :param low: minimum endpoint
        :param high: maximum endpoint
        :return: the number of keys in the symbol table between low (inclusive) and high (inclusive)
        """
        if low is None:
            raise KeyError("first argument to size() is null")
        if high is None:
            raise KeyError("second argument to size() is null")

        if self.__compare(low, high) > 0:
            return 0
        if high in self:
            return self.rank(high) - self.rank(low) + 1
        else:
            return self.rank(high) - self.rank(low)






