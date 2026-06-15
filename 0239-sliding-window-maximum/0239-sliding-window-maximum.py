from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        my_deque = deque()
        ans = []
        for i in range(0,len(nums)):
            while len(my_deque) > 0 and my_deque[0] <= i - k:
                my_deque.popleft()
            while len(my_deque) > 0 and nums[i] > nums[my_deque[-1]]:
                my_deque.pop()
            my_deque.append(i)
            if (i >= k-1):
                ans.append(nums[my_deque[0]])
        return ans




       



        
       
            


                

            



        