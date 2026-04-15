class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        ans = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(0,len(nums)):
            if i%2 == 0:
                ans.append(even[0])
                even.remove(even[0])
            else:
                ans.append(odd[0])
                odd.remove(odd[0])
        return ans


        