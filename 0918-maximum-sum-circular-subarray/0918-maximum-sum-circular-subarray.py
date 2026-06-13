class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_max = max_sum = nums[0]
        for num in nums[1:]:
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
        # If all elements are negative
        if max_sum < 0:
            return max_sum
        # Kadane for minimum subarray
        cur_min = min_sum = nums[0]
        for num in nums[1:]:
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
        return max(max_sum, total - min_sum)
