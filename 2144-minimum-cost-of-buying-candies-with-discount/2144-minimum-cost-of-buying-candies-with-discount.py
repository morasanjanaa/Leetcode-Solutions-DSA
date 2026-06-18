class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        buy = 0
        for i in range(len(cost)-1,-1,-1):
            if buy < 2:
                buy += 1
                ans += cost[i]
            else:
                buy = 0
        return ans






        