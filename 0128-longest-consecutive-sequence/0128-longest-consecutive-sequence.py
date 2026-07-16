class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        longest = 0

        for i in arr:
            if i-1 not in arr:
                length = 0
                while(i+length in arr):
                    length+=1
                longest = max(longest,length)
        return longest

        
        '''
        if not nums:
            return 0
        nums.sort()
        cur = 1
        max_len = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i-1]+1 == nums[i]:
                cur+=1
                max_len = max(max_len,cur)
            else:
                cur = 1
        return max_len
        '''

        