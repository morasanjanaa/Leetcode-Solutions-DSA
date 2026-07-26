class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Recursive Aproach Practice
        def find(i,target):
            if i == len(nums):
                return -1

            if nums[i] == target:
                return i

            return find(i+1,target)

        return find(0,target)


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