from collections import namedtuple
from typing import List

PileItem = namedtuple('PileItem', ['i', 'left_pile_item'])


def bottom_up_solution(nums: List[int]) -> List[int]:
    dp = [1 for _ in nums]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] >= nums[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    result = []
    curr_count = max(dp)
    curr_num = -1
    # traversing the answer
    for i in range(len(nums) - 1, -1, -1):
        if curr_count == 0:
            break
        if dp[i] == curr_count and curr_num <= nums[i]:
            result.append(i + 1)  # 1-based index
            curr_count -= 1
            curr_num = nums[i]
    return result[::-1]


def patience_sort_solution(nums: List[int]) -> List[int]:
    if not nums:
        return []
    piles = []
    for i in range(len(nums)):
        add_num(i, piles, nums)
    result = []
    cur_pile_item = piles[-1][-1]
    while cur_pile_item:
        result.append(cur_pile_item.i + 1)  # 1-based index
        cur_pile_item = cur_pile_item.left_pile_item
    return result[::-1]


def add_num(index: int, piles: List[List[PileItem]], nums: List[int]):
    num = nums[index]
    lo, hi = 0, len(piles)
    while lo < hi:
        mid = (hi + lo) // 2
        if num > nums[piles[mid][-1].i]:
            # move left
            hi = mid
        else:
            # move right
            lo = mid + 1
    if lo == len(piles):
        piles.append([])
    piles[lo].append(
        PileItem(index, piles[lo - 1][-1] if lo > 0 else None)
    )


if __name__ == '__main__':
    input()
    input_nums = [int(s) for s in input().split(' ')]
    res = patience_sort_solution(input_nums)
    print(len(res))
    print(' '.join(str(i) for i in res))
