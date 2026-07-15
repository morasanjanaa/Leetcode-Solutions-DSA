from typing import List
from functools import lru_cache

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        @lru_cache(None)
        def backtrack(open_left, close_left):

            if open_left == 0 and close_left == 0:
                return [""]

            ans = []

            if open_left > 0:
                for s in backtrack(open_left - 1, close_left):
                    ans.append("(" + s)

            if close_left > open_left:
                for s in backtrack(open_left, close_left - 1):
                    ans.append(")" + s)

            return ans

        return backtrack(n, n)