class Solution:  
    def rob(self, nums: List[int]) -> int:
        #Constant space
        n = len(nums)
        prevprev = 0
        prev = nums[0]
        for i in range(2,n+1):
            if i-2 > 0:
                steal = nums[i-1] + prevprev
            else:
                steal = nums[i-1]
            skip = prev
            temp = max(skip,steal)
            prevprev = prev
            prev = temp
        return prev

        

        