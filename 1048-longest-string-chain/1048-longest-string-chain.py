from functools import lru_cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPred(cur,prev):
            cur_len = len(cur)
            prev_len = len(prev)

            if prev_len + 1 != cur_len:
                return False

            i,j = 0,0
             
            while(i<prev_len and j<cur_len):
                if cur[j] == prev[i]:
                    i+=1
                j+=1

            return i == prev_len
        # Bottom Up solution
        words.sort(key=len)
        n = len(words)
        dp = [1]*n
        maxi = 1
        for i in range(n):
            for j in range(i):
                if isPred(words[i],words[j]):
                    dp[i] = max(dp[i],dp[j]+1)
                    maxi = max(maxi,dp[i])
        return maxi

 


        '''
        ----Recursion + memorization
        def isPred(cur,prev):
            cur_len = len(cur)
            prev_len = len(prev)

            if prev_len + 1 != cur_len:
                return False

            i,j = 0,0
             
            while(i<prev_len and j<cur_len):
                if cur[j] == prev[i]:
                    i+=1
                j+=1

            return i == prev_len

        @lru_cache(None)
        def solve(cur_idx,prev_idx):

            if cur_idx >= len(words):
                return 0

            if prev_idx != -1 and dp[cur_idx][prev_idx] != -1:
                return dp[cur_idx][prev_idx]

            skip = solve(cur_idx+1,prev_idx)
            take = 0

            if prev_idx == -1 or isPred(words[cur_idx],words[prev_idx]):
                take = 1 + solve(cur_idx+1,cur_idx)

            if prev_idx != -1:
                dp[cur_idx][prev_idx] = max(skip,take)

            return max(skip,take)

        words.sort(key=len)
        n = len(words)
        dp = [[-1] * (n+1) for _ in range(n+1)]
        return solve(0,-1)
        '''