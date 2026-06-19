class Solution:
    def findLongestChain(self, nums: List[List[int]]) -> int:
        nums.sort()
        n = len(nums)
        dp = [1]*(n+1)
        maxi = 1
        for i in range(n):
            for j in range(i):
                if nums[j][1] < nums[i][0]:
                    dp[i] = max(dp[i],dp[j]+1)
                    maxi = max(dp[i],maxi)
        return maxi
        


        