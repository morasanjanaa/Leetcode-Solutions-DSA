from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements = Counter(nums)
        target = len(nums) // 3
        ans = []
        for element, count in elements.items():
            if count > target:
                ans.append(element)
        return ans

        