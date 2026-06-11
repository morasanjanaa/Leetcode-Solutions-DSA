class Solution:
    def maxArea(self, nums: List[int]) -> int:
        max_area = float('-inf')
        i = 0
        j = len(nums)-1
        while(i<=j):
            area = min(nums[i],nums[j])
            max_area = max(max_area,area*(j-i))
            if nums[i] < nums[j]:
                i+=1
            else:
                j-=1
        return max_area
