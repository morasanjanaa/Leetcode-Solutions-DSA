class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        size = len(bloomDay)

        if(size < m * k):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while(low<=high):
            mid = (low+high)//2
            got = 0
            b = 0

            for i in bloomDay:
                if i<=mid:
                    got +=1

                    if got == k:
                        b += 1
                        got = 0
                else:
                    got = 0
                
            if b >= m:
                high = mid - 1
            else:
                low = mid + 1
                
        return low
            

        