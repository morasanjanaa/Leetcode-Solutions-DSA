class Solution:
    def solve(self,nums,i,dp,n):
        # Recursion + Memorization
        if i > n:
            return 0
        if dp[i] != -1:
            return dp[i]
        steal = nums[i] + self.solve(nums,i+2,dp,n)
        skip = self.solve(nums,i+1,dp,n)
        dp[i] = max(steal,skip)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return max(nums)
        
        dp = [-1] * 100
        # case 1 - Take first house 0th index house
        zero_steal = self.solve(nums,0,dp,n-2)
        dp = [-1] * 100
        # Case 2 - Take Second House 1th index house
        one_steal = self.solve(nums,1,dp,n-1)
        return max(one_steal,zero_steal)
    


        