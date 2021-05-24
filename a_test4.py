#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    visited = [False for _ in related]
    res = 0
    for i, _ in enumerate(related):
        res += dfs(related, i, visited)
    return res


def dfs(related, i, visited):
    if visited[i]:
        return 0
    visited[i] = True

    for j, _ in enumerate(related):
        if i == j:
            continue
        if related[i][j] != '0' or related[j][i] != '0':
            dfs(related, j, visited)
    return 1


if __name__ == '__main__':
    pass
