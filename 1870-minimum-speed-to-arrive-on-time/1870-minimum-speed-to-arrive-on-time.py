from math import ceil
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist) - 1
        
        if hour <= n:
            return -1

        low = 1
        high = 10**7
        ans = -1

        while low <= high:

            mid = (low + high) // 2

            time = 0

            for i in range(n):
                time += ceil(dist[i] / mid)

            time += dist[-1] / mid

            if time <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans