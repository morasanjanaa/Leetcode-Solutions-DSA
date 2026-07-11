class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []  # stores indices

        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                idx = stack.pop()
                ans[idx] = nums[i % n]

            # Push indices only during the first pass
            if i < n:
                stack.append(i)

        return ans