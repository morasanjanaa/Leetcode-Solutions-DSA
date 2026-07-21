class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows > len(s) :
            return s
        rows = [""]*numRows
        cur = 0
        d = -1
        for ch in s:
            rows[cur] += ch
            if cur==0 or cur==numRows-1:
                d *= -1
            cur += d
        return "".join(rows)
        