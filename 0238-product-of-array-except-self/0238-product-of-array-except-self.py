class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]*len(nums)
        postfix_product = [1]*len(nums)
        ans = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix_product[i] = nums[i-1]*prefix_product[i-1]
        for i in range(len(nums)-2,-1,-1):
            postfix_product[i] = nums[i+1]*postfix_product[i+1]
        for i in range(0,len(nums)):
            ans[i] = prefix_product[i] * postfix_product[i]
        return ans


           






      
       
