class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for element in A:
            result.append(element * element)
        
        result.sort()
        return result