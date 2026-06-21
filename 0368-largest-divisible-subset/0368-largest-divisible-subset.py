from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        dp = [1] * n          # Length of largest divisible subset ending at i
        parent = [-1] * n     # To reconstruct the subset

        max_len = 1
        last_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                last_index = i

        # Reconstruct the subset
        ans = []
        while last_index != -1:
            ans.append(nums[last_index])
            last_index = parent[last_index]

        return ans[::-1]
        '''
        nums.sort()
        n = len(nums)

        @lru_cache(None)
        def solve(i, prev):
            if i == n:
                return ()

            # Skip current element
            skip = solve(i + 1, prev)

            # Take current element if divisible
            take = ()
            if prev == -1 or nums[i] % nums[prev] == 0:
                take = (nums[i],) + solve(i + 1, i)

            if len(take) > len(skip):
                return take
            return skip

        return list(solve(0, -1))
        '''