from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        got = Counter()
        min_len = float('inf')
        ans = ""
        count = 0
        for right in range(0,len(s)):
            ch = s[right]
            if ch in need:
                got[ch] += 1
                if got[ch] <= need[ch]:
                    count += 1  
            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right- left + 1
                    ans = s[left:right+1]
                if s[left] in need:
                    got[s[left]] -= 1
                    if got[s[left]] < need[s[left]]:
                        count -= 1
                left += 1
        return ans

            
        return ans




        