from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        #Botom up
        m = len(s1)
        n = len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
            
        '''
        @lru_cache(None)
        def solve(i,j):
            if i >= m or j >= n:
                return 0
            if s1[i] == s2[j]:
                return 1 + solve(i+1,j+1)
            return max(solve(i+1,j),solve(i,j+1))
        m = len(s1)
        n = len(s2)
        return solve(0,0)
        '''

        