from structures.red_black_bst import RedBlackBST


class MyCalendar:
    EVENT_START = 1
    EVENT_END = 2
    EVENT_START_AND_END = 3

    def __init__(self):
        self.tree = RedBlackBST()

    def book(self, start: int, end: int) -> bool:
        if start >= end:
            raise Exception('start should be greater than end.')
        end -= 1

        if self.tree:
            # check events on the left
            if self.tree.min() <= start and (self.tree[self.tree.floor(start)] == self.EVENT_START):
                return False

            # check events on the right
            if self.tree.max() >= end and (self.tree[self.tree.ceiling(end)] == self.EVENT_END):
                return False

            # check in the middle
            for _ in self.tree.keys(start, end):
                return False

        if start == end:
            self.tree[start] = self.EVENT_START_AND_END
        else:
            self.tree[start] = self.EVENT_START
            self.tree[end] = self.EVENT_END
        return True


if __name__ == '__main__':
    cal = MyCalendar()
    print(cal.book(0, 1))
    print(cal.book(0, 1))
