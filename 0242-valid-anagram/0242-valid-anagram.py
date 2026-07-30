from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(s)
        for i in t :
            if i in freq :
                freq[i] -= 1
                if freq[i] == 0 :
                    del freq[i]
            else:
                return False
        return len(freq) == 0

        
            

        