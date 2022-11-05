from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        for start, end in firstList:
            search_intersections(secondList, start, end, res)
        return res


def search_intersections(intervals: List[List[int]], start: int, end: int, res: List[List[int]]) -> None:
    lo, hi = 0, len(intervals) - 1
    while lo < hi:
        mid = (hi + lo) // 2
        other_start, other_end = intervals[mid]
        if other_end < start:
            lo = mid + 1
        else:
            hi = mid
    for i in range(lo, len(intervals)):
        other_start, other_end = intervals[i]
        if other_start > end or other_end < start:
            break
        res.append(intersection(start, end, other_start, other_end))


def intersection(start1: int, end1: int, start2: int, end2: int) -> List[int]:
    return [max(start1, start2), min(end1, end2)]


if __name__ == '__main__':
    print(Solution().intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]]
    ))
