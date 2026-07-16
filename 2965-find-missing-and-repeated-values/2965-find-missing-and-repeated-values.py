class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = {}
        repeat = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in seen:
                    repeat = grid[i][j]
                seen[grid[i][j]] = True
            for i in range(1, len(grid)*len(grid[0])+1):
                if i not in seen:
                    missing = i
                    break
        return repeat, missing
        