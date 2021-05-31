from typing import List, Tuple

from utils import print_grid, CellPrintFormat


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        nums.sort(reverse=True)
        # return bottom_up_solution(nums, nums_sum, k)

        partition_sum = nums_sum // k
        used_numbers_bit_mask = 0
        cache = {}
        for i in range(k):
            res, used_numbers_bit_mask = top_down_solution(nums, partition_sum, used_numbers_bit_mask, cache)
            if not res:
                return False
        return True


def top_down_solution(nums: List[int], partition_target: int, used_numbers_bit_mask: int, cache: dict) -> Tuple[bool, int]:
    if partition_target == 0:
        return True, used_numbers_bit_mask

    if (partition_target, used_numbers_bit_mask) not in cache:
        for i, n in enumerate(nums):
            # number already in use or is greater than target
            if n > partition_target or 1 << i & used_numbers_bit_mask != 0:
                continue
            res, used_nums = top_down_solution(nums, partition_target - n, used_numbers_bit_mask | (1 << i), cache)
            if res:
                return res, used_nums
        cache[(partition_target, used_numbers_bit_mask)] = False
    return cache[(partition_target, used_numbers_bit_mask)], 0


def bottom_up_solution(nums: List[int], nums_sum: int, k: int) -> bool:
    partition_sum = nums_sum // k
    dp = [
        [False for _ in range(partition_sum + 1)] for _ in nums
    ]
    nums_used_bit_masks = [
        [0 for _ in range(partition_sum + 1)] for _ in nums
    ]

    global_nums_used_bit_mask = 0

    # iterate over partitions
    for p in range(1, k + 1):

        # reset dp for the next partition
        for i, _ in enumerate(dp):
            for j, _ in enumerate(dp[i]):
                dp[i][j] = j == 0
                nums_used_bit_masks[i][j] = 0

        for curr_sum in range(1, partition_sum + 1):
            curr_sum_solved = False
            curr_nums_used_bit_mask = 0
            for i, num in enumerate(nums):
                if not curr_sum_solved and (1 << i) & global_nums_used_bit_mask == 0:
                    if num == curr_sum:
                        curr_sum_solved = True
                        curr_nums_used_bit_mask |= 1 << i
                    elif i > 0 and curr_sum > num and ((1 << i) & nums_used_bit_masks[i - 1][curr_sum - num]) == 0:
                        curr_sum_solved = dp[i - 1][curr_sum - num]
                        if curr_sum_solved:
                            curr_nums_used_bit_mask = (1 << i) | nums_used_bit_masks[i - 1][curr_sum - num]
                dp[i][curr_sum] = curr_sum_solved
                nums_used_bit_masks[i][curr_sum] = curr_nums_used_bit_mask

        # print('{0} partition #{1} {0}'.format('-' * 10, p))
        # print_grid(nums_used_bit_masks, name='nums_used_bit_masks', cell_format=CellPrintFormat.BINARY)
        # print_grid(dp, name='dp')
        # print(nums)
        # check if solved current partition
        if not dp[-1][-1]:
            return False

        # include numbers used in current partition
        global_nums_used_bit_mask |= nums_used_bit_masks[-1][-1]

    # print_grid(nums_used_bit_masks, name='nums_used_bit_masks', cell_format=CellPrintFormat.BINARY)
    # print_grid(dp, name='dp')
    # print(nums)
    return True


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(Solution().canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4))
    print(Solution().canPartitionKSubsets([4, 4, 6, 2, 3, 8, 10, 2, 10, 7], 4))
