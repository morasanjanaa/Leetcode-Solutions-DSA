class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        seen = dict()
        total = 0
        seen[0] = -1
        for i in range(0,len(nums)):
            total += nums[i]
            rem = total % k
            if rem in seen:
                if i - seen[rem] >= 2:
                    return True
            else:
                seen[rem] = i
        return False

            

        

             

        