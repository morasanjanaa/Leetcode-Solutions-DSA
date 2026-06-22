class Solution:  
    def rob(self, nums: List[int]) -> int:
        # Bottom up
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2,n+1):
            take = 0
            if i-2 >= 0:
                take = dp[i-2] + nums[i-1]
            skip = dp[i-1]
            dp[i] = max(skip,take)
        return dp[n]
            





        '''
        # Recursion + memorization
        def solve(i,dp):
            if i >= len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]
            skip = solve(i+1,dp)
            take = nums[i] + solve(i+2,dp)
            dp[i] = max(skip,take)
            return max(skip,take)
        dp = [-1]*len(nums)
        return solve(0,dp)

        #Constant space
        n = len(nums)
        prevprev = 0
        prev = nums[0]
        for i in range(2,n+1):
            if i-2 > 0:
                steal = nums[i-1] + prevprev
            else:
                steal = nums[i-1]
            skip = prev
            temp = max(skip,steal)
            prevprev = prev
            prev = temp
        return prev
        '''

        

        