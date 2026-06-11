class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr_ans = 0
        for i in nums:
            if(i==1):
                curr_ans+=1
            else:
                ans = max(curr_ans,ans)
                curr_ans = 0
        return max(curr_ans,ans)
