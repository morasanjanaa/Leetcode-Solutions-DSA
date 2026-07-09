class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        low = 1
        high = pos[-1] - pos[0]
        while(low <= high):
            mid = (low + high) // 2
            last = pos[0]
            place = 1
            for i in range(1,len(pos)):
                if pos[i] - last >= mid:
                    place += 1
                    last = pos[i]
            if place >= m:
                low = mid + 1
            else:
                high = mid - 1
        return high

