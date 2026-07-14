class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       size = len(nums)
       pre = 1
       post = 1
       result = [0]*size
       for i in range(0,size):
             if(i==0):
                result[i]=1
             else:
                pre = nums[i-1] *pre
                result[i] = pre
       for i in range(size-1,-1,-1):
              if(i==size-1):
                result[i] = post*result[i]
              else:
                post = post*nums[i+1]
                result[i]=result[i]*post
       return result

       '''
        prefix_product = [1]*len(nums)
        postfix_product = [1]*len(nums)
        ans = [1]*len(nums)
        #nums = [1,2,3,4]
        #left-sum : prefix_sum [1,1,2,6]
        for i in range(1,len(nums)):
            prefix_product[i] = nums[i-1]*prefix_product[i-1]
        #right-sum : postfix_sum [24,12,4,1]
        for i in range(len(nums)-2,-1,-1):
            postfix_product[i] = nums[i+1]*postfix_product[i+1]
        for i in range(0,len(nums)):
            ans[i] = prefix_product[i] * postfix_product[i]
        return ans
        '''


           






      
       
