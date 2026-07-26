class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)

        n = len(nums)
        mid = (n + 1) // 2

        left = arr[:mid]
        right = arr[mid:]

        i = len(left) - 1
        j = len(right) - 1

        for k in range(0, n, 2):
            nums[k] = left[i]
            i -= 1

        for k in range(1, n, 2):
            nums[k] = right[j]
            j -= 1