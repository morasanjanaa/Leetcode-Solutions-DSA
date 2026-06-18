from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0] = maximum alternating sum ending with a subtraction (even state)
        # dp[i][1] = maximum alternating sum ending with an addition (odd state)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(1, n + 1):
            # Even state
            dp[i][0] = max(dp[i - 1][1] - nums[i - 1],
                           dp[i - 1][0])
            # Odd state
            dp[i][1] = max(dp[i - 1][0] + nums[i - 1],
                           dp[i - 1][1])

        return max(dp[n][0], dp[n][1])