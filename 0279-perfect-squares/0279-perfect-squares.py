class Solution:
    def numSquares(self, n: int):

        def help(n):
            if n == 0:
                return 0

            if dp[n] != -1:
                return dp[n]

            mini = float('inf')

            i = 1
            while i * i <= n:
                mini = min(mini, 1 + help(n - i * i))
                i += 1

            dp[n] = mini
            return mini

        dp = [-1] * (n + 1)
        return help(n)