class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]):

        one_len = len(nums1)
        two_len = len(nums2)

        dp = [[0] * (two_len + 1) for _ in range(one_len + 1)]

        maxi = 0

        for i in range(1, one_len + 1):
            for j in range(1, two_len + 1):

                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxi = max(maxi, dp[i][j])

        return maxi