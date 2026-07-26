class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )


        '''
        res = []

        def dfs(i, picked, product):
            if picked == 3:
                res.append(product)
                return

            if i == len(nums):
                return

            # Pick current element
            dfs(i + 1, picked + 1, product * nums[i])

            # Don't pick current element
            dfs(i + 1, picked, product)

        dfs(0, 0, 1)
        return max(res)
        '''