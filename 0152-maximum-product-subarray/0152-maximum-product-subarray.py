class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxi,mini = 1,1
        for i in nums:
            temp = maxi * i
            maxi = max(temp,i,i*mini)
            mini = min(temp,i,i*mini)
            res = max(res,maxi)
        return res
       