import enum
from time import time
from typing import List


def print_execution_time(name: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time()
            try:
                return func(*args, **kwargs)
            finally:
                print('{}:\t\t{}s'.format(name, round(time() - start, 2)))
        return wrapper
    return decorator


class CellPrintFormat(enum.Enum):
    DECIMAL = 0
    BINARY = 1


def print_grid(grid: List[List[int]], name: str = None, cell_format: CellPrintFormat = CellPrintFormat.DECIMAL):
    print('-' * len(grid) * 5 + ' ' + (name or '') + ' ' + '-' * len(grid) * 5)
    for i, row in enumerate(grid):
        if i == 0:
            if cell_format == CellPrintFormat.BINARY:
                print('   ' + ''.join('|{:>10}'.format(x) for x in range(len(row))))
            else:
                print('   ' + ''.join('|{:>5}'.format(x) for x in range(len(row))))
        row_str = '{:>3}'.format(i)
        for j, c in enumerate(row):
            if cell_format == CellPrintFormat.BINARY:
                row_str += '|{:0>10}'.format(bin(c)[2:])
            else:
                row_str += '|{:>5}'.format(c)
        print(row_str)


