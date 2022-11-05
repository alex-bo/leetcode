from typing import List
import bisect
import utils


class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        # return rotate_clockwise_transpose(matrix)
        # return rotate_clockwise_inplace(matrix)
        return rotate_counter_clockwise_transpose(
            rotate_counter_clockwise_transpose(
                rotate_counter_clockwise_transpose(
                    matrix
                )
            )
        )


def rotate_clockwise_transpose(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
    return matrix


def rotate_clockwise_inplace(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = tmp
    return matrix


def rotate_counter_clockwise_transpose(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    for i in range(n):
        for j in range(n - i - 1):
            matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
    return matrix


def reflect_vertically(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
    return matrix


def reflect_horizontally(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    return matrix


if __name__ == '__main__':
    # grid = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    # ]
    grid = [
        [1,   2,  3,  4],
        [5,   6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16],
    ]
    utils.print_grid(grid, 'original')
    utils.print_grid(Solution().rotate([r.copy() for r in grid]), 'rotated')
    utils.print_grid(reflect_vertically([r.copy() for r in grid]), 'reflected vertically')
    utils.print_grid(reflect_horizontally([r.copy() for r in grid]), 'reflected horizontally')
