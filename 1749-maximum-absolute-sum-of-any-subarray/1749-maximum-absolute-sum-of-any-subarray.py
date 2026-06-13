class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_max = 0
        cur_min = 0
        maxi = 0
        mini = 0
        for i in range(0,len(nums)):
            cur_max = max(cur_max+nums[i],nums[i])
            maxi = max(cur_max,maxi)

            cur_min = min(nums[i]+cur_min,nums[i])
            mini = min(cur_min,mini)
        return max(abs(maxi),abs(mini))

        