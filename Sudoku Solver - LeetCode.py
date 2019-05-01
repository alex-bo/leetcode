from typing import List, Tuple
# from time import time


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solve(0, 0, board)


# global_time = dict(time=time())


def solve(ii: int, jj: int, board: List[List[str]]) -> bool:
    i, j = next_empty(ii, jj, board)
    if i is not None and j is not None:
        for n in range(1, 10):
            if not can_put(str(n), i, j, board):
                continue
            board[i][j] = str(n)
            # if time() - global_time['time'] > 0:
            #     print('=========================')
            #     print_rect(board)
            #     global_time['time'] = time()
            # print('board[{}][{}] = {}'.format(i, j, n))
            if solve(i, j, board):
                return True
            board[i][j] = '.'
    else:
        return not has_empty(board)
    return False


def has_empty(board):
    for i in board:
        for j in i:
            if j == '.':
                return True
    return False


def next_empty(ii: int, jj: int, board: List[List[str]]) -> Tuple[int, int]:
    for i in range(ii, len(board)):
        for j in range(jj, len(board[i])):
            if board[i][j] == '.':
                return i, j
        jj = 0
    return None, None


def can_put(nn: str, ii: int, jj: int, board: List[List[str]]) -> bool:
    # horizontal
    for n in board[ii]:
        if n == nn:
            return False
    # vertical
    for i in range(len(board)):
        if board[i][jj] == nn:
            return False
    # local square
    for i in range(ii // 3 * 3, ii // 3 * 3 + 3):
        for j in range(jj // 3 * 3, jj // 3 * 3 + 3):
            if board[i][j] == nn:
                return False
    return True


def print_rect(board: List[List[str]]):
    for i in board[:3]:
        print(''.join(i[:3]), ' ', ''.join(i[3:6]), ' ', ''.join(i[6:9]))
    print()
    for i in board[3:6]:
        print(''.join(i[:3]), ' ', ''.join(i[3:6]), ' ', ''.join(i[6:9]))
    print()
    for i in board[6:9]:
        print(''.join(i[:3]), ' ', ''.join(i[3:6]), ' ', ''.join(i[6:9]))


def test():
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],

        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],

        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    print_rect(board)
    Solution().solveSudoku(board)
    print_rect(board)


if __name__ == '__main__':
    pass
    # test()
