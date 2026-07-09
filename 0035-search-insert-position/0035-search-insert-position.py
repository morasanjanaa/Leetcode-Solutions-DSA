class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == target:
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return low