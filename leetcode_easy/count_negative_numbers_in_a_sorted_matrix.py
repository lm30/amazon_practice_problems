class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        negCount = 0
        maxRow = len(grid)
        maxCol = len(grid[0]) - 1
        
        # going from right to left because matrix sorted in non increasing order
        col = maxCol
        row = 0        

        while row < maxRow:
            if col < 0 or grid[row][col] >= 0:
                row += 1
                col = maxCol
            else:
                col -= 1
                negCount += 1
        
        return negCount