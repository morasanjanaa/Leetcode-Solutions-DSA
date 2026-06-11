class Solution:
    def trap(self, nums: List[int]) -> int:
        max_l = 0
        max_r = 0
        i = 0
        j = len(nums)-1
        ans = 0
        while(i<j):
            if nums[i] < nums[j]:
                max_l = max(max_l,nums[i])
                ans += max_l - nums[i]
                i+=1 
            else:
                max_r = max(max_r,nums[j])
                ans += max_r - nums[j]
                j-=1
        return ans