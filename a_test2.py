from time import time


def minimumDays(rows, columns, grid):
    days = 0
    src = [[grid[r][c] for c in range(columns)] for r in range(rows)]
    dst = [[0 for c in range(columns)] for r in range(rows)]
    while doUpgrade(src, dst) > 0:
        src, dst = dst, src
        days += 1
    return days


def doUpgrade(src, dst):
    upgraded = 0
    for i, row in enumerate(src):
        for j, cell in enumerate(row):
            if cell == 1:
                dst[i][j] = 1
            else:
                if (
                        (i > 0 and src[i - 1][j] == 1) or  # top
                        (i < (len(src) - 1) and src[i + 1][j] == 1) or  # bottom
                        (j > 0 and src[i][j - 1] == 1) or  # left
                        (j < (len(row) - 1) and src[i][j + 1] == 1)  # right
                ):
                    dst[i][j] = 1
                    upgraded += 1
                else:
                    dst[i][j] = 0
    return upgraded


def minimumDaysBFS(rows, columns, grid):
    grid = [[grid[r][c] for c in range(columns)] for r in range(rows)]
    day1_queue = []
    days = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                day1_queue.append((i, j))
    while True:
        day2_queue = []
        while day1_queue:
            i, j = day1_queue.pop()
            try_add_to_queue(grid, i - 1, j, day2_queue)
            try_add_to_queue(grid, i, j - 1, day2_queue)
            try_add_to_queue(grid, i + 1, j, day2_queue)
            try_add_to_queue(grid, i, j + 1, day2_queue)
        if not day2_queue:
            break
        day1_queue = day2_queue
        days += 1
    return days


def try_add_to_queue(grid, i, j, queue):
    if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 0:
        queue.append((i, j))
        grid[i][j] = 1


def main():
    large_grid = []
    for i in range(100):
        large_grid.append([0] * 100)
    large_grid[-1][-1] = 1
    grids = [[
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ],
        large_grid
    ]

    for grid in grids:
        tm = time()
        minDays = minimumDays(len(grid), len(grid[0]), grid)
        naive_time = time() - tm
        tm = time()
        minDaysBFS = minimumDaysBFS(len(grid), len(grid[0]), grid)
        bfs_time = time() - tm

        print('grid={}x{}'.format(len(grid), len(grid[0])))
        print('minDays={} ({}s)'.format(minDays, naive_time))
        print('minDaysBFS={} ({}s)'.format(minDaysBFS, bfs_time))


if __name__ == '__main__':
    main()
