class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(0,len(numbers)):
            need = target - numbers[i]
            if need in seen:
                return [seen[need]+1,i+1]
            else:
                seen[numbers[i]] = i
        return -1

        