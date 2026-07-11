class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapi = {}

        for num in nums2:
            while stack and num > stack[-1]:
                mapi[stack.pop()] = num
            stack.append(num)

        while stack:
            mapi[stack.pop()] = -1

        ans = []
        for num in nums1:
            ans.append(mapi[num])

        return ans