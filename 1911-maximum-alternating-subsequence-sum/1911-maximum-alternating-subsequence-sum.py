class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n+1)]
        for i in range(1,n+1):
            # Here Even Case = Take front_odd - nums , Skip-front even remains
            dp[i][0] = max(dp[i-1][1] - nums[i-1],dp[i-1][0])
            # Odd case = Take front_even + nums ,skip-front odd-remains
            dp[i][1] = max(dp[i-1][0] + nums[i-1],dp[i-1][1])

        return max(dp[n][0],dp[n][1])
