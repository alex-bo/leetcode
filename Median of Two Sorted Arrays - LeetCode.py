from time import time
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = int(half_len - i)
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


        # easy solution
        # time: O((n+m)*log(n+m))
        # space: O(n+m)
        # nums3 = sorted(nums1 + nums2)
        # if len(nums3) % 2 == 0:
        #     return (nums3[int(len(nums3)/2)] + nums3[int(len(nums3)/2)-1]) / 2
        # return nums3[int(len(nums3)/2)]


def main():
    test(2.0, [1, 3], [2])
    test(2.5, [1, 2], [3, 4])


def test(expected, *args) -> None:
    start = time()
    error = False
    actual = 0
    try:
        actual = Solution().findMedianSortedArrays(*args)
    except:
        error = True
        raise
    result = 'SUCCESS'
    if error:
        result = 'EXCEPTION'
    elif actual != expected:
        result = 'FAIL expected {} got {}'.format(expected, actual)
    print(('twoSum({args}) = {actual}\t'
           '{time}s\t'
           '{result}').format(
        args=args,
        actual=actual,
        time=round(time() - start, 1),
        result=result
    ))


if __name__ == '__main__':
    main()
