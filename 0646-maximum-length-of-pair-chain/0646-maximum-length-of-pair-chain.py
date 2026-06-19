class Solution:
    def findLongestChain(self, nums: List[List[int]]) -> int:
        def solve(i,P,dp):
            if i >= len(nums):
                return 0

            if P!=-1 and dp[i][P] != -1:
                return dp[i][P]

            skip = solve(i+1,P,dp)
            take = 0

            if P == -1 or nums[i][0] > nums[P][1]:
                take = 1 + solve(i+1,i,dp)

            if P != -1:
                dp[i][P] = max(skip,take)

            return max(skip,take)
            
        nums.sort()
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        return solve(0,-1,dp)


        