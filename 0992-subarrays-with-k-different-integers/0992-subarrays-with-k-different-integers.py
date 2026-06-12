from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            left = 0
            freq = defaultdict(int)
            ans = 0
            for right in range(len(nums)):
                freq[nums[right]] += 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                ans += right - left + 1
            return ans      
        # Exactly K
        result = atMostK(nums, k) - atMostK(nums, k - 1)
        return result
                


        