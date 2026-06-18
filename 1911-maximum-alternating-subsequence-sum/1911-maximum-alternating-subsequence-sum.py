from functools import lru_cache
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        @lru_cache(None)
        def solve(i, flag):
            if i == len(nums):
                return 0

            skip = solve(i + 1, flag)

            val = nums[i] if flag else -nums[i]
            take = val + solve(i + 1, not flag)

            return max(skip, take)

        return solve(0, True)