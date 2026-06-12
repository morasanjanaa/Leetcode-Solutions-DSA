class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = dict()
        cur_sum = 0
        result = 0
        freq[0] = 1
        for i in range(0,len(nums)):
            cur_sum += nums[i]
            need = cur_sum-k
            if (need in freq):
                result += freq[need]
            freq[cur_sum] = freq.get(cur_sum,0)+1
        return result