class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        mini = min(nums)
        maxi = max(nums)
        seen = set(nums)
        if maxi < 0:
            return 1
        for i in range(1,maxi+2):
            if i not in seen and i > 0:
                return i
        










        '''
        n = len(nums)
        seen = [False] * (n + 1)  
        for num in nums:
            if 0 < num <= n:
                seen[num] = True
        for i in range(1, n + 1):
            if (seen[i]==False):
                return i
        return n + 1
        '''