from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
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

        