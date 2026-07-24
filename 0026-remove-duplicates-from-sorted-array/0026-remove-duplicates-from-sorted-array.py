class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        start = 0
        for i in range (0,size):
            if(nums[start]!= nums[i]):
                start = start + 1
                nums[start] = nums[i]
        return start+1