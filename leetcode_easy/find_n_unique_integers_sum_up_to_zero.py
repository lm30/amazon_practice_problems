class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        result = []
        if n % 2 == 1: # if odd then add a zero to result list
            result.append(0)
            n -= 1
        
        while n > 0:
            result.append(n)
            result.append(n * -1)
            n -= 2
        
        return result