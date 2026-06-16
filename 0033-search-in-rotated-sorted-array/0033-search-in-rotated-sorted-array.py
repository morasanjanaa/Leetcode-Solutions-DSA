class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        def binarySearch(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        pivot = findPivot(nums)
        ans = binarySearch(0, pivot - 1)
        if ans != -1:
            return ans
        return binarySearch(pivot, len(nums) - 1)