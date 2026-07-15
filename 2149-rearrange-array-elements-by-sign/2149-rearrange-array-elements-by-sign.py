class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg = []
        pos = []
        ans = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        i = 0
        j = 0
        temp = 0

        while(temp<len(nums)):
            if temp%2==0:
                ans.append(pos[i])
                i += 1
            else:
                ans.append(neg[j])
                j += 1
            temp += 1

        return ans
    
            

       





        