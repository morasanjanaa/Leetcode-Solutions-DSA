from typing import List

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
      from typing import List

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(h)):
            while stack and h[stack[-1]] > h[i]:
                element = h[stack.pop()]
                nse = i

                if stack:
                    pse = stack[-1]
                else:
                    pse = -1

                max_area = max(max_area, element * (nse - pse - 1))

            stack.append(i)   # <-- Missing in your code

        while stack:
            element = h[stack.pop()]
            nse = len(h)

            if stack:
                pse = stack[-1]
            else:
                pse = -1

            max_area = max(max_area, element * (nse - pse - 1))

        return max_area

        '''
        def previousSmallest(h):
            pse = [-1]*len(h)
            stack = []
            for i in range(0,len(h)):
                while stack and h[stack[-1]] >= h[i]:
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                stack.append(i)
            return pse

        def nextSmallest(h):
            nse = [len(h)]*len(h)
            stack = []
            for i in range(len(h)-1,-1,-1):
                while stack and h[stack[-1]] >= h[i]:
                    stack.pop()
                if stack:
                    nse[i] = stack[-1]
                stack.append(i)
            return nse
        
        pse = previousSmallest(heights)
        nse = nextSmallest(heights)

        ans = 0
        for i in range(len(heights)):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            ans = max(ans, area)

        return ans
        '''
            

