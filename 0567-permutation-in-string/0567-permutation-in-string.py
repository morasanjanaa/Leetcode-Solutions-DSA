from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        for i in range(0,len(s2)):
            freq = Counter(s2[i:i+len(s1)])
            if freq == need:
                return True
        return False
        


        