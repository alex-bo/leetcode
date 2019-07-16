from collections import namedtuple
from typing import Set, Tuple


Item = namedtuple('Item', ['value', 'frequency'])


class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = dict()

    def push(self, x: int) -> None:
        """Find place to put using custom comparator and binary search."""
        self.counter[x] = self.counter.setdefault(x, 0) + 1
        new_item = Item(value=x, frequency=self.counter[x])
        self.stack.insert(self.__binary_search_index(new_item), new_item)

    def __binary_search_index(self, new_item: Item) -> int:
        min_ = 0
        max_ = len(self.stack) - 1
        while True:
            if max_ < min_:
                return min_
            middle = (min_ + max_) // 2
            curr_item = self.stack[middle]
            if new_item.frequency >= curr_item.frequency:
                # if new item frequency higher or the same as current, go right
                min_ = middle + 1
            else:
                # new item frequency lower, go left
                max_ = middle - 1

    def pop(self) -> int:
        item = self.stack.pop()
        self.counter[item.value] = self.counter[item.value] - 1
        if self.counter[item.value] <= 0:
            del self.counter[item.value]
        return item.value


class FreqStackNotOptimized:

    def __init__(self):
        self.stack = []
        self.counter = dict()

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.counter[x] = self.counter.setdefault(x, 0) + 1

    def pop(self) -> int:
        freq_nums = self.__get_freq_numbers()
        for i in range(len(self.stack)):
            i = len(self.stack) - i - 1
            if self.stack[i] in freq_nums:
                x = self.stack.pop(i)
                self.counter[x] = self.counter[x] - 1
                return x
        raise Exception('Stack is empty.')

    def __get_freq_numbers(self) -> Set[int]:
        if not self.counter:
            return set()
        s = sorted(self.counter.items(), key=lambda pair: pair[1], reverse=True)
        freq_top = s[0][1]
        result = set()
        for i, (k, v) in enumerate(s):
            if freq_top != v:
                break
            result.add(k)
        return result


def test():
    test_one(["push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
             [5, 7, 5, 7, 4, 5], [5, 7, 5, 4])


def test_one(operations: list, push_nums: list, pop_nums_expected: list):
    print(operations)
    print(push_nums)
    stack = FreqStack()
    for op in operations:
        if op == 'push':
            print(op)
            print(push_nums[0])
            stack.push(push_nums.pop(0))
            print(stack.stack)
        elif op == 'pop':
            actual = stack.pop()
            expected = pop_nums_expected.pop(0)
            if actual == expected:
                print('OK')
            else:
                print('WRONG! Got {}, expected {}.'.format(actual, expected))
                break
        else:
            raise Exception('Unsupported operation.')


if __name__ == '__main__':
    test()
