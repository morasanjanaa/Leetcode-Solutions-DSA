class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        i = 0
        n = len(nums)

        while i< n-1 and nums[i] == nums[i+1]:
            i += 3

        return nums[i]

        