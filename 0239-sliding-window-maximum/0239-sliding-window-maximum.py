from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       # step 1 when new element comes it has to be in window and size is <=k
       # step 2 if greater comes then pop all left
       # step 3 push deques elements
       # step 4 if window size is == k append dequeue(front)
            mono_deque = deque()
            ans = list()
            for i in range(0,len(nums)):
                # step 1: make space for new elements(vaid window)
                while len(mono_deque)>0 and mono_deque[0] <= i-k:
                    mono_deque.popleft()
                # step 2 pop small elements
                while len(mono_deque)>0 and nums[i] > nums[mono_deque[-1]]:
                    mono_deque.pop()
                # step 3 push greater element to dequeue
                mono_deque.append(i)
                #step 4 get ans maximum from deque from start index
                if (i>= k-1):
                    ans.append(nums[mono_deque[0]])
            return ans




        
       
            


                

            



        