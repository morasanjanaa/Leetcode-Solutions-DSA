class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        ans = 0
        product = 1
        for right in range(0,len(nums)):
           product *= nums[right]
           while(left < len(nums) and product >= k):
              product //= nums[left]
              left += 1
           ans += right - left + 1
        return ans
        
        

        