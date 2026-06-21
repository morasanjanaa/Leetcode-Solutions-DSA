from functools import lru_cache
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        @lru_cache(None)
        def solve(i, prev):
            if i == n:
                return ()

            # Skip current element
            skip = solve(i + 1, prev)

            # Take current element if divisible
            take = ()
            if prev == -1 or nums[i] % nums[prev] == 0:
                take = (nums[i],) + solve(i + 1, i)

            if len(take) > len(skip):
                return take
            return skip

        return list(solve(0, -1))