class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        openParen = 0
        closedParen = 0
        
        for letter in S:
            if letter == "(":
                openParen += 1
            elif letter == ")":
                if openParen <= 0:
                    closedParen += 1
                else:
                    openParen -= 1

        return openParen + closedParen