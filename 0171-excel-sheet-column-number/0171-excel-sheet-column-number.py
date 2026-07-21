class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            val = ord(i)-ord("A")+1
            res = res * 26 + val
        return res