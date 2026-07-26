from functools import lru_cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        @lru_cache(None)
        def generate(left,right,s):
            if right == n:
                res.append(s)
            if left < n:
                generate(left+1,right,s+"(")
            if right < left:
                generate(left,right+1,s+")")
        generate(0,0,"")
        return res
        