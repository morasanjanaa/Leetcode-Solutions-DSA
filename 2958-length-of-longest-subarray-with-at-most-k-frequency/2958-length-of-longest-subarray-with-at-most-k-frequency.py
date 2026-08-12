class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = dict()
        low = 0
        ans = 0
        for high in range(len(nums)):
            freq[nums[high]] = freq.get(nums[high],0)+1
            while(freq[nums[high]]>k):
                freq[nums[low]] -= 1
                if freq[nums[low]] == 0:
                    del freq[nums[low]]
                low += 1
            ans = max(ans,high - low + 1)
        return ans
        
            



        
        