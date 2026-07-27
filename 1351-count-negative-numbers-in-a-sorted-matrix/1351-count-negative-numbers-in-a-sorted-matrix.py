class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_num = 0
        for row in grid:
            for col in row:
                if col < 0:
                    neg_num += 1
        return neg_num
        