class Solution:
    def solve(self,nums,i,dp):
        # Recursion + Memorization
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        steal = nums[i] + self.solve(nums,i+2,dp)
        skip = self.solve(nums,i+1,dp)
        dp[i] = max(steal,skip)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.solve(nums,0,dp)
    


        