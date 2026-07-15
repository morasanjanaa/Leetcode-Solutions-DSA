class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        ans = [1]*len(nums)

        #Calculate Prefix

        for i in range(1,len(nums)):
            ans[i] = pre * nums[i-1]
            pre = ans[i]

        #Calculate Postfix along with ans

        for i in range(len(nums)-2,-1,-1):
            ans[i] = post * nums[i+1] * ans[i]
            post = post * nums[i+1]
        return ans
        