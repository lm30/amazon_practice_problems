class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "X":
                    if row == 0 or board[row - 1][col] == ".":
                        if col == 0 or board[row][col - 1] == ".":
                            count += 1
        return count