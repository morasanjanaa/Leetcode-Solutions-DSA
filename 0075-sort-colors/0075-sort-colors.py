class Solution:
    def sortColors(self, arr: List[int]) -> None:
        # Dutch Flag Algorithm
        low = 0
        high = len(arr)-1
        mid = 0

        while mid <= high:
            
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                mid += 1
                low += 1

            elif arr[mid] == 1:
                mid += 1

            else:
                arr[high],arr[mid] = arr[mid],arr[high]
                high -= 1

