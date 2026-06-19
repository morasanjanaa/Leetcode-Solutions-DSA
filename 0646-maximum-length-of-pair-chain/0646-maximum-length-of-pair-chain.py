class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 0
        prev = float('-inf')
        for i,j in pairs:
            if prev < i:
                res += 1
                prev = j
        return res

        ''' DP Bottom up
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
        '''
        


        