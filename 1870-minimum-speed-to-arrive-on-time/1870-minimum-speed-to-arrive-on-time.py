from math import ceil
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right = 1, 10**7
        res = -1

        while left <= right:
            mid = (left + right) // 2

            total_time = 0

            # First n-1 trains (must wait for the next integer hour)
            for i in range(len(dist) - 1):
                total_time += ceil(dist[i] / mid)

            # Last train (no waiting after it)
            total_time += dist[-1] / mid

            if total_time <= hour:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res