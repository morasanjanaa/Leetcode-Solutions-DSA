class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_product = 1
        right_product = 1
        left_max = float("-inf")
        right_max = float('-inf')
        for i in nums:
            left_product *= i
            left_max = max(left_max,left_product)
            if left_product == 0:
                left_product = 1
        for i in range(len(nums)-1,-1,-1):
            right_product *= nums[i]
            right_max = max(right_max,right_product)
            if right_product == 0:
                right_product = 1
        return max(left_max,right_max)
        
        
    

        