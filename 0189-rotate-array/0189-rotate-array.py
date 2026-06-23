class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k %= n

        # Reverse entire array
        reverse(0, n - 1)

        # Reverse first k elements
        reverse(0, k - 1)

        # Reverse remaining elements
        reverse(k, n - 1)