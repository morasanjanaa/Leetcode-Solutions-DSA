class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def Atmost(nums,k):
            odd = 0
            left = 0
            ans = 0
            for right in range(0,len(nums)):
                if nums[right] % 2 == 1:
                    odd += 1
                while(odd > k):
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1
                ans += right - left + 1
            return ans
        return Atmost(nums,k) - Atmost(nums,k-1) 
        