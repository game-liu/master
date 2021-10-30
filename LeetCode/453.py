# 一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
from typing import List


class Solution(object):

    def minMoves(self, nums: List[int]) -> int:
        min_n = min(nums)
        res = 0
        for num in nums:
            res = res + num - min_n
        return res

    def minMoves_1(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)


if __name__ == "__main__":
    nums = [1, 2, 5]
    res = Solution().minMoves_1(nums)
    print(res)
