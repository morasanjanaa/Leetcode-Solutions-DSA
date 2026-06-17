class Solution:
    def solve(self,n,nums):
            if n < 2:
                return n
            if nums[n] != -1:
                return nums[n]
            nums[n] = self.solve(n-1,nums) + self.solve(n-2,nums)
            return nums[n]
        
    def fib(self, n: int) -> int:
        nums = [-1] * (n+1)
        return self.solve(n,nums)
        


        