class Solution:
    def solve(self,n,dp):
        if n == 1 or n == 2:
            return n
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.solve(n-1,dp) + self.solve(n-2,dp)

        return dp[n]

    def climbStairs(self, n: int) -> int:
           if n == 1 or n == 2:
            return n
           dp = [-1]*(n+1)
           dp[1] = 1
           dp[2] = 2
           return self.solve(n,dp)


