class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if i == len(nums):
                res.append(curr)
                return

            dfs(i + 1, curr + [nums[i]])  # Pick
            dfs(i + 1, curr)              # Don't Pick

        dfs(0, [])
        return res