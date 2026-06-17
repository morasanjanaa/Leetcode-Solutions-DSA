class Solution:  
    def rob(self, nums: List[int]) -> int:
        # Bottom Up Solution
        n = len(nums)
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2,n+1):
            if i-2 > 0:
                steal = nums[i-1] + dp[i-2]
            else:
                steal = nums[i-1]
            skip = dp[i-1]
            dp[i] = max(skip,steal)
        return dp[n]


    


        