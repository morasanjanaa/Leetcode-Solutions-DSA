class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_ans = 0
        ans = 0
        for i in nums:
            if i == 1:
                cur_ans += 1
                ans = max(ans,cur_ans)
            else:
                cur_ans = 0
        return ans

       