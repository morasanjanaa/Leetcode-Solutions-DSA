class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def givesubsets(i, ans):
            if i == len(nums):
                res.append(ans[:])   # store a copy
                return

            # Pick
            ans.append(nums[i])
            givesubsets(i + 1, ans)

            # Backtrack
            ans.pop()

            # Don't pick
            givesubsets(i + 1, ans)

        givesubsets(0, [])
        return res