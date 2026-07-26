class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg_arr = []
        pos_arr = []
        
        for i in nums:
            if i < 0:
                neg_arr.append(i)
            else:
                pos_arr.append(i)
        i = 0
        pos = 0
        neg = 0
        arr = [-1]*len(nums)
        
        while(i < len(nums)):
            if i%2 == 0:
                arr[i] = pos_arr[pos]
                pos += 1
            else:
                arr[i] = neg_arr[neg]
                neg += 1
            i += 1
       
        return arr


















        '''
        pos_index=0
        neg_index=1

        ans=[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]<0:
                ans[neg_index]=nums[i]
                neg_index+=2
            else:
                ans[pos_index]=nums[i]
                pos_index+=2

        return ans
        '''