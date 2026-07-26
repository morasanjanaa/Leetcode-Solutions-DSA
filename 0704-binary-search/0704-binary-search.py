class Solution:
    def search(self, arr: List[int], target: int) -> int:
        # Recursive Aproach Practice
        def find(low,high,target):
            if low  > high:
                 return -1

            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                return find(low,mid-1,target)
            else:
                return find(mid + 1,high,target)
        
        return find(0,len(arr)-1,target)


        '''
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if(nums[mid]==target):
                return mid
            elif(target<nums[mid]):
                high = mid-1
            else:
                low = mid+1
        return -1
        '''