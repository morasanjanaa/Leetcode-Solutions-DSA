class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       size = len(nums)
       low = 0
       high = size-1
       while(low<=high):
        mid = (low+high)//2
        #left greater
        if(mid>0 and nums[mid]<nums[mid-1]):
            high = mid-1
        elif(mid<size-1 and nums[mid]<nums[mid+1]):
            low = mid+1
        else:
            return mid

       
      
        
        
   