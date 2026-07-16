class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(arr)
        cols = len(arr[0])
        row = [False]*rows
        col = [False]*cols

        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(rows):
            for j in range(cols):
                if row[i] or col[j]:
                    arr[i][j] = 0

        
                
        